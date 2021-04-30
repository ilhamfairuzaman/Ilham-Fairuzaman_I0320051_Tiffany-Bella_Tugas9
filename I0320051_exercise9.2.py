import sys

#define array asosiatif
KAMUS = {
    'one':'satu',
    'two':'dua',
    'three':'tiga',
    'four':'empat',
    'five':'lima',
    'six':'enam',
    'seven':'tujuh',
    'eight':'delapan',
    'nine':'sembilan',
    'ten':'sepuluh',
}

def main():
    #input user
    kata = input('Masukkan kata dalam bahasa inggris\n>>> ')

    if not kata in KAMUS.keys():
        print("'%s' tidak ditemukan di dalam kamus ini" % kata)
        sys.exit(1)

    print("arti kata '%s' adalah '%s'" % (kata, KAMUS[kata]))


if __name__ == "__main__":
    main()