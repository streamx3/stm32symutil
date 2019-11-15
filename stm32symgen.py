#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Andrii Shelestov"
__copyright__ = "Copyright 2019, OpenSource"
__license__ = "MIT"
__version__ = "0.1"
__email__ = "streamx3@gmail.com"

import os
import sys
import getopt
import platform
from openpyxl import Workbook
from xml.etree import ElementTree as ET


PATH = ''

PATH_CUBEMX = ''  #'/home/s13/Install/STM32CubeMX/'
PATH_CUBEIDE = ''  #'/opt/st/stm32cubeide_1.0.2/'

PATH_CUBEMX_MAC = ''
PATH_CUBEIDE_MAC = ''

PATH_CUBEMX_WIN = ''
PATH_CUBEIDE_WIN = ''

systems_fixedpath = ['Darwin', 'Windows']
systems_supported = ['Darwin', 'Windows', 'Linux']

URL_GITHUB = 'https://github.com/streamx3/stm32symutil'

alt_func = ['all', 'none', 'first']
alt_func_list = ['spi', 'sdmmc', 'i2c', 'uart', 'usart', 'usb', 'swd', 'jtag', 'tim', 'sai', 'tsc', 'adc', 'rcc', 'wkup']
# 'spi,sdmmc,i2c,uart,usart,usb,swd,jtag,tim,sai,tsc,adc,rcc'
input_opts = ['mcu=', 'af=', 'af_split=', 'power_split=', 'outfile=', 'help', 'version', 'mxpath=', 'idepath=']
usage_opts = '--mcu MCU_name --af Alt_Func\n\t--power=Power_Align--outfile=OutFile\nExamples:\n' + \
             '\t--mcu [STM32F103C8Tx/STM32L552MEYxQ] -- you can type in both upper and\n\t\tlower case, ' + \
                'ommit x and everything that goes after that,\n\t\tbut onlyif anything after "x" is not ambiguous\n' +\
             '\t--af [all/none/first] or a list like spi,sdmmc,i2c,uart,usart,usb,swd,' +\
             '\n\t\tjtag,tim,sai,tsc,adc,rcc,wkup\n' +\
             '\t--af_split [y/n/yes/no] -- splits selected alternative functions\n\t\tin different columns\n' +\
             '\t--power_split [y/n/yes/no] -- if split selected, power pins will be put\n\t\tseparately below,' +\
             ' so they could be put into separate symbol\n' +\
             '\t--outfile [FILE] -- output filename for spreadsheet. ' +\
             '\n\t\tIf it\'s not ending with *.xlsx -- it\'ll be added for you.\n' +\
             '\t--help -- display this help\n' +\
             '\t--version -- displays program\'s version\n' +\
             '\t--mxpath [PATH] -- temporal path to CubeMX on Linux\n' \
             '\t--idepath [PATH] -- temporal path to CubeIDE on Linux'

MCU = ''
AF = 'first'
AF_LIST = []
AF_SPLIT = False
POWER_SPLIT = False
OUTFILE = ''


def usage():
    print(sys.argv[0] + usage_opts)
    sys.exit(2)


def check_known_files_presence(path):
    failures = 0
    known_files = ['compatibility.xml', 'defines', 'families.xml', 'rules.xml', 'STM32F103C(8-B)Tx.xml']
    for file in known_files:
        tmp = path + os.path.sep + file
        if os.path.exists(tmp) and os.path.isfile(tmp):
            pass
        else:
            failures += 1

    if failures == 0:
        return True
    else:
        return False


def locate_internal_mx(path):
    content = os.listdir(path)
    for c in content:
        if c.startswith('com.st.stm32cube.common.mx_'):
            return c
    return None


def mcufile2names(fname):
    if '(' in fname and ')' in fname:
        arr = fname.split('(')
        prefix = arr[0]
        tmp = arr[1].split(')')
        vars = tmp[0]
        suffix = tmp[1]
        vars = vars.split('-')
        rv = []
        for v in vars:
            rv.append(prefix + v + suffix)
        # print(rv)
        return rv
    else:
        return [fname]


def namecmp(found, given):
    l_found = len(found)
    l_given = len(given)
    l = l_given if l_given < l_found else l_found
    for i in range(l):
        if found[i] != 'x':
            if found[i].lower() != given[i].lower():
                return False
    return True


if __name__ == '__main__':
    # Empty opt's check
    if len(sys.argv) < 2:
        usage()
        sys.exit()

    # Parse options:
    try:
        optlist, arglist = getopt.getopt(sys.argv[1:], 'hv', input_opts)
    except getopt.GetoptError as err:
        print(err)
        usage()
    for o, a in optlist:
        # print('o: ' + o + '\ta: ' + a)
        if '--help' == o or '-h' == o:
            usage()
        if '--mcu' == o:
            MCU = a
        if '--af' == o:
            if a in alt_func:
                AF = a
            else:
                # print(a)
                final_af_list = []
                tmp_list = a.split(',')
                # print(tmp_list)
                for tmp in tmp_list:
                    if tmp in alt_func_list:
                        final_af_list.append(tmp)
                if len(final_af_list) > 0:
                    AF = 'list'
                    AF_LIST = final_af_list
                print('Validated Alternative Function options:')
                print(AF_LIST)
        if '--af_split' == o:
            if a.lower() in ['y', 'yes', 'yeah']:
                AF_SPLIT = True
        if '--power' == o:
            if a.lower() in ['y', 'yes', 'yeah']:
                POWER_SPLIT = True
        if '--outfile' == o:
            if not a.endswith('.xlsx'):
                a += '.xlsx'
            OUTFILE = a
            print('OUTFILE: ' + OUTFILE)
        if '--version' == o or '-v' == o:
            print('Version: ' + __version__)
            print('Author : ' + __author__)
            print('License: ' + __license__)
            sys.exit(0)
        if '--mxpath' == o:
            PATH_CUBEMX = a
        if '--idepath' == o:
            PATH_CUBEIDE = a

    # OS detection
    system = platform.system()
    print('Dectected OS: ' + system)
    if system in systems_fixedpath:
        if system == 'Darwin':
            PATH_CUBEMX = PATH_CUBEMX_MAC
            PATH_CUBEIDE = PATH_CUBEIDE_MAC
        elif system == 'Windows':
            PATH_CUBEMX = PATH_CUBEMX_WIN
            PATH_CUBEIDE = PATH_CUBEIDE_WIN
    else:
        if system in systems_supported:
            if PATH == '' and PATH_CUBEMX == '' and PATH_CUBEIDE == '':
                print('You\'re using Linux, so you should open this file and set one or both of first 2 variables,',
                      'which are:\n' +
                      '\tPATH_CUBEMX - path to CubeMX, e.g:"/.../STM32CubeMX/"\n' +
                      '\tPATH_CUBEIDE - path to CubeIDE, e.g:"/.../STM32CubeIDE/"\n\n' +
                      'Restart this program after doing so. Cube MX will be preferred if both set.\n' +
                      'Alternatively use --mxpath or --idepath')
                sys.exit(-1)

    # Path verification
    if PATH == '':
        TMP = PATH_CUBEMX
        if TMP[-1:] != os.path.sep:
            TMP += os.path.sep
        if system == 'Darwin':
            TMP += 'Contents/Resources/'
        TMP += 'db' + os.path.sep + 'mcu' + os.path.sep
        if os.path.exists(PATH_CUBEMX) and os.path.isdir(PATH_CUBEMX) and os.path.exists(TMP) and os.path.isdir(TMP):
            if check_known_files_presence(TMP):
                PATH = TMP

        if PATH == '':
            if os.path.exists(PATH_CUBEIDE) and os.path.isdir(PATH_CUBEIDE):
                TMP = PATH_CUBEIDE
                if TMP[-1:] != os.path.sep:
                    TMP += os.path.sep
                if system == 'Darwin':
                    TMP += 'Contents/Eclipse/'
                TMP += 'plugins' + os.path.sep
                internal_mx = locate_internal_mx(TMP)
                if internal_mx is None:
                    print('CubeMX not found and CubeIDE was not parsed correctly.\n' +
                          'Please install CubeMX or report a bug:\n' + URL_GITHUB)
                    sys.exit(-1)
                TMP += internal_mx + os.path.sep + 'db' + os.path.sep + 'mcu' + os.path.sep
                if os.path.exists(TMP) and os.path.isdir(TMP):
                    if check_known_files_presence(TMP):
                        PATH = TMP
        if PATH == '':
            if system == 'Linux':
                print('Found nothing. Make sure you\'ve set PATH or give and installed CubeMX or CubeIDE.\n' +
                      'Or, if you suspect a bug -- feel free to report it:\n' + URL_GITHUB)
            elif system in systems_fixedpath:
                print('Found nothing. Make sure you\'ve installed CubeMX or CubeIDE.\n' +
                      'If you\'re sure CubeMX or CubeIDE is installed -- please report a bug:\n' + URL_GITHUB)
            else:
                print('Well, you are the one who uses this script in ' + system + ' environment.\n' +
                      'What is the deal with ' + system + ' anyway?\n' +
                      'Probable cause of your problen is a lack of ST\'s CUBE software or wrong a  path.\n' +
                      'But you probably know what you\'re doing, so good luck!')
            sys.exit(-1)
    print('Using PATH: ' + PATH)

    # MCU search
    print('Searching for: ' + MCU.upper())
    files_list = os.listdir(PATH)
    d_mcus = {}
    for f in files_list:
        f_red = f.replace('.xml', '')
        if f.startswith('STM32'):
            d_mcus[f] = mcufile2names(f_red)
    mcus_found = []
    for k in d_mcus:
        for tmp_mcu in d_mcus[k]:
            if namecmp(tmp_mcu, MCU):
            # if tmp_mcu.replace('x', '').lower().startswith(MCU.lower()):
                if k not in mcus_found:
                    mcus_found.append(k)
    if len(mcus_found) == 0:
        print('MCU not found!')
        sys.exit(0)
    if len(mcus_found) > 1:
        print('Found ' + str(len(mcus_found)) + ' MCUs:')
        for m in mcus_found:
            print(m)
        print('Provide more specific input!')
        sys.exit(0)
    if len(mcus_found) == 1:
        print('Successfully found 1 MCU: ' + mcus_found[0])

    # Parsing XML
    tree = ET.parse(PATH + os.path.sep + mcus_found[0])
    root = tree.getroot()
    tag = root.tag
    # print(tag)
    # print(type(tag))
    table = {}
    for ch1 in root:
        t = ch1.tag.replace('{http://mcd.rou.st.com/modules.php?name=mcu}', '')
        attrib = ch1.attrib
        # print(t, attrib)
        if t == 'Pin':
            af = []
            for ch2 in ch1:
                t = ch2.tag.replace('{http://mcd.rou.st.com/modules.php?name=mcu}', '')
                # print(t, ch2.attrib)
                att2 = ch2.attrib
                if 'Name' in att2:
                    if AF == 'list':
                        for a in AF_LIST:
                            ch2name = ch2.attrib['Name']
                            if ch2name.lower().find(a) > -1:
                                af.append(ch2.attrib['Name'])
                    if AF in ['all', 'first']:
                        af.append(ch2.attrib['Name'])
                        if AF == 'first':
                            break

            pos = attrib['Position']
            del attrib['Position']
            attrib['af'] = af
            table[pos] = attrib
    # Printing table
    wb = Workbook()
    ws = wb.active
    ws['A1'] = 'Designator'
    ws['B1'] = 'Electrical Type'
    ws['C1'] = 'Display Name'
    i = 2
    for k in table:
        elType = table[k]['Type'].replace('Reset', 'Input').replace('MonoIO', 'Power')
        ws['A' + str(i)] = k
        ws['B' + str(i)] = elType
        ws['C' + str(i)] = table[k]['Name']
        i += 1
        if AF_SPLIT:
            pass
        else:
            pass
    wb.save(OUTFILE)


