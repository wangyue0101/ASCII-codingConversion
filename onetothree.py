import click
import sys
import enum
import re

from metaStr import meta


Etype = {
    "hex": 0,
    "dec": 1,
    "oct": 2,
}
ALLOWABLE_ENCODE_TYPE = ("dec", "oct", "hex", "html_dec", "html_hex", "url")
ALLOWABLE_DECODE_TYPE = ("de_dec", "de_html_dec", "de_hex", "de_html_hex", "de_url")


def get_encode_str(t, e_type):
    for i in t:
        if i not in meta.keys():
            print("字符串编码出错，请输入正确的字符串")
            sys.exit()

        yield meta[i][e_type]


def get_decode_str(target, dtype):
    keys_list = [_ for _ in list(meta.keys())]
    values_list = [i[dtype] for i in list(meta.values())]
    position = 0

    while position < len(target):
        if target[position] == "1":
            if target[position:position+3] in values_list:
                index = values_list.index(target[position:position+3])
                position += 3
        else:
            if target[position:position+2].upper() in values_list:
                index = values_list.index(target[position:position+2].upper())
                position += 2

        yield keys_list[index]


@click.command()
@click.option("-e", help="编码类型(八进制/oct，十进制/dec，十六进制/hex, HTML十进制/html_dec， HTML十六进制/html_hex,")
@click.option("-d", help="解码类型(十进制解码/de_dec，HTML十进制解码/de_html_dec，十六进制解码/de_hex，HTML十六进制解码/de_html_hex)")
@click.option("-t", help="需要转换的字符串")
def main(e, d, t):
    if not e and not d:
        print("请使用 \"python onetothree.py --help\" 查看使用说明")
        sys.exit()
    if e and d:
        print("请使用 \"python onetothree.py --help\" 查看使用说明")
        sys.exit()
    if not t:
        print("请使用 \"python onetothree.py --help\" 查看使用说明")
        sys.exit()

    result = ""
    if e:
        if e not in ALLOWABLE_ENCODE_TYPE:
            print("请使用 \"python onetothree.py --help\" 查看使用说明")
            sys.exit()

        if e == "dec":                  # 十进制编码
            result = (i for i in get_encode_str(t, Etype["dec"]))
        elif e == "oct":                # 八进制编码
            result = (i for i in get_encode_str(t, Etype["oct"]))
        elif e == "hex":                # 十六进制编码
            result = (i for i in get_encode_str(t, Etype["hex"]))
        elif e == "html_dec":           # HTML十进制编码
            result = ("&#"+i+";" for i in get_encode_str(t, Etype["dec"]))
        elif e == "html_hex":           # HTML十六进制编码
            result = ("&#x"+i+";" for i in get_encode_str(t, Etype["hex"]))
        elif e == "url":                # URL ENCODE
            result = ("%"+i for i in get_encode_str(t, Etype["hex"]))

        # TODO JS编码

    if d:
        if d not in ALLOWABLE_DECODE_TYPE:
            print("请使用 \"python onetothree.py --help\" 查看使用说明")
            sys.exit()

        if d == "de_hex":               # 十六进制解码
            result = (i for i in get_decode_str(t, Etype["hex"]))
        elif d == "de_html_hex":        # HTML十六进制解码
            t = "".join(re.split(r"[&#x;]", t))
            result = (i for i in get_decode_str(t, Etype["hex"]))
        elif d == "de_dec":             # 十进制解码
            result = (i for i in get_decode_str(t, Etype["dec"]))
        elif d == "de_html_dec":        # HTML十进制解码
            t = "".join(re.split(r"[&#;]", t))
            result = (i for i in get_decode_str(t, Etype["dec"]))
        elif d == "de_url":             # URL解码
            t = "".join(re.split(r"[%]", t))
            result = (i for i in get_decode_str(t, Etype["hex"]))

        # TODO JS解码

    print("".join(list(result)))


if __name__ == "__main__":
    main()
