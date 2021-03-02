import re
import itertools

sample_string = "m1e-2_mu1e-6_r1e-6_sigsqr25_N500.png"


def create_friendly_param(text):
    text_parts = ["".join(x) for _, x in itertools.groupby(text, str.isdigit)]
    param = text_parts[0]
    opt = "".join(text_parts[1:])
    param_opt = "{}={}".format(param, opt)
    return param_opt


def create_friendly_label(path):
    opt_string = path.replace('.png', "")
    opts = opt_string.split('_')
    friendly_opts = [create_friendly_param(p) for p in opts]
    return ", ".join(friendly_opts)


def create_latex_string(path, parent_dir):
    friendly_label = create_friendly_label(path)
    latex_imgpath = "{}/{}".format(parent_dir, path)

    string = f"\\begin{{figure}}[h]\n\t\\caption*{{{friendly_label}}}\n\t\\centering\n\t\\includegraphics[width=\\textwidth]{{{latex_imgpath}}}\n\\end{{figure}}"

    return string