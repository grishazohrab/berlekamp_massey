from berlekamp_massey import BerlekampMassey

import argparse


args_parser = argparse.ArgumentParser()
args_parser.add_argument("--seq", type=str, required=True, help="Input sequence")
args_parser.add_argument("--mod", type=int, default=0, help="Modulo of arithmetic")


if __name__ == '__main__':
    bm_args = args_parser.parse_args()
    input_seq = [int(x) for x in bm_args.seq.split(",")]
    mod = bm_args.mod
    bm = BerlekampMassey(mod)
    register_len = bm(input_seq)
    print(f"The length of register is {register_len}")
    print("End")