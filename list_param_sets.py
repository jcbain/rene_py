import argparse
from creators import creators

default_migr = ["0.1" ,"5e-2", "1e-2", "5e-3", "1e-3", "5e-4", "1e-4", "1e-5"]
default_mut = ["1e-6", "1e-5", "1e-4"]
default_recomb = ["0.00625"]
default_sigsqr = ["2", "10", "5", "15", "25"]
default_n = ["100", "500", "1000", "5000"]

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-m', '--migrations', nargs='+', action='store', type=str, default=default_migr)
    parser.add_argument('-x', '--mutations', nargs='+', action='store', type=str, default=default_mut)
    parser.add_argument('-r', '--recombinations', nargs='+', action='store', type=str, default=default_recomb)
    parser.add_argument('-s', '--sigsqrs', nargs='+', action='store', type=str, default=default_sigsqr)
    parser.add_argument('-n', '--pops', nargs='+', action='store', type=str, default=default_n)

    results = parser.parse_args()

    m_opts = creators.create_params("m=", *results.migrations)
    mu_opts = creators.create_params("mu=", *results.mutations)
    r_opts = creators.create_params("r=", *results.recombinations)
    sigsqr_opts = creators.create_params("sigsqr=", *results.sigsqrs)
    n_opts = creators.create_params("n=", *results.pops)

    perms = creators.create_permutations(m_opts, mu_opts, r_opts, sigsqr_opts, n_opts)

    for perm in perms:
        print(' '.join([f'--{opt}' for opt in perm]))


if __name__ == "__main__":
    main()
