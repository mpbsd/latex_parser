#!/usr/bin/env python3


import re


regex = {
    "math": {
        "i": {
            0: re.compile(r"\$([^$]+)\$", re.DOTALL),
            1: re.compile(r"\\\((.*?)\\\)", re.DOTALL),
        },
        "d": {
            0: re.compile(r"\${2}([^$]+)\${2}", re.DOTALL),
            1: re.compile(r"\\\[(.*?)\\\]", re.DOTALL),
        },
    },
}


mathmode = {
    "i": {"opening": r"\(", "closing": r"\)"},
    "d": {"opening": r"\[", "closing": r"\]"},
}


def parser(file: str):
    try:
        with open(file, "r") as f:
            g = f.read()
            g = regex["math"]["d"][0].sub(r"\\[\1\\]", g)
            g = regex["math"]["i"][0].sub(r"\\(\1\\)", g)
            E = {
                "i": regex["math"]["i"][1].findall(g),
                "d": regex["math"]["d"][1].findall(g),
            }
            with open("brew/parsed.tex", "w") as h:
                for eq_t in ["i", "d"]:
                    for eq in E[eq_t]:
                        formatted_eq = "{}\n\t{}\n{}".format(
                            mathmode[eq_t]["opening"],
                            re.sub(r"\s+", r" ", eq),
                            mathmode[eq_t]["closing"],
                        )
                        print(formatted_eq, file=h)
        return None
    except IOError:
        print("File does not exist.")
        return None


def main():
    parsed_latex_file = parser("brew/main.tex")
    print(parsed_latex_file)


if __name__ == "__main__":
    main()
