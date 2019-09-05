import click
import sys
import enum

from metaStr import meta

Etype = {
    "hex": 0,
    "dec": 1,
    "oct": 2,
}


def get_encode_str(t, e_type):
    for i in t:
        if i not in meta.keys():
            print("字符串编码出错，请输入正确的字符串")
            sys.exit()

        yield meta[i][e_type]


def get_decode_str(target, dtype):
    keys = [_ for _ in list(meta.keys())]
    hex_values = [i[dtype] for i in list(meta.values())]

    for i in range(int(len(target)/2)):
        if target[i*2:i*2+2].upper() in hex_values:
            index = hex_values.index(target[i*2:i*2+2].upper())
            yield keys[index]


@click.command()
@click.option("-e", help="转换后的类型(八进制/oct，十进制/dec，十六进制/hex, HTML十进制/html_dec， HTML十六进制/html_hex,"
                          " 解码十六进制/de_hex)")
@click.option("-t", help="需要转换的字符串")
def main(e, t):
    if e not in ("dec", "oct", "hex", "html_dec", "html_hex", "de_hex") or (not e or not t):
        print("请使用 \"python onetothree.py --help\" 查看使用说明")
        sys.exit()

    result = ""

    if e == "dec":      # 十进制编码
        result = (i for i in get_encode_str(t, Etype["dec"]))
    elif e == "oct":        # 八进制编码
        result = (i for i in get_encode_str(t, Etype["oct"]))
    elif e == "hex":        # 十六进制编码
        result = (i for i in get_encode_str(t, Etype["hex"]))
    elif e == "html_dec":       # HTML十进制编码
        result = ("&#"+i+";" for i in get_encode_str(t, Etype["dec"]))
    elif e == "html_hex":       # HTML十六进制编码
        result = ("&#x"+i+";" for i in get_encode_str(t, Etype["hex"]))
    elif e == "de_hex":     # 十六进制解码
        result = (i for i in get_decode_str(t, Etype["hex"]))

    print("".join(list(result)))


if __name__ == "__main__":
    main()
