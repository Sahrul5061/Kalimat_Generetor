# import os

# # Memastikan kata.txt ada dan dapat dibaca
# if not os.path.exists('kata.txt'):
#     print("File kata.txt tidak ditemukan.")
# else:
#     # Membaca isi file kata.txt
#     with open('kata.txt', 'r', encoding='utf-8') as f:
#         # Membaca semua baris dalam file kata.txt
#         kata_lines = f.readlines()

#     # Membuka hasil.txt untuk menulis
#     try:
#         with open('hasil.txt', 'w', encoding='utf-8') as f_output:
#             # Proses setiap baris di kata.txt
#             for kata in kata_lines:
#                 # Membersihkan whitespace atau newline dari setiap baris
#                 kata_cleaned = kata.strip()

#                 if kata_cleaned:  # Pastikan kata tidak kosong
#                     # Template dengan longtail keyword
#                     article_template = (
#                         f"berikan saya artikel dengan longtail keyword \"{kata_cleaned}\" "
#                         "mengandung seo dan banyak mengandung kata dari longtail keywordnya "
#                         "tanpa di bold dan anti duplikasi sebanyak 1000 kata,\n"
#                     )

#                     # Menulis hasil ke dalam hasil.txt
#                     f_output.write(article_template)
#                 else:
#                     print("Baris kosong ditemukan di kata.txt, melewati baris ini.")
#         print("Hasil artikel telah disimpan di hasil.txt.")
#     except Exception as e:
#         print(f"Terjadi kesalahan saat menulis ke hasil.txt: {e}")
import os

# Memastikan kata.txt ada dan dapat dibaca
if not os.path.exists('kata.txt'):
    print("File kata.txt tidak ditemukan.")
else:
    # Membaca isi file kata.txt
    with open('kata.txt', 'r', encoding='utf-8') as f:
        # Membaca semua baris dalam file kata.txt
        kata_lines = f.readlines()

    # Membuka hasil.txt untuk menulis
    try:
        with open('hasil.txt', 'w', encoding='utf-8') as f_output:
            # Proses setiap baris di kata.txt
            for kata in kata_lines:
                # Membersihkan whitespace atau newline dari setiap baris
                kata_cleaned = kata.strip()

                if kata_cleaned:  # Pastikan kata tidak kosong
                    # Template dengan longtail keyword, mengganti teks placeholder
                    article_template = (
                        f"berikan saya artikel dengan longtail keyword \"{kata_cleaned}\" "
                        f"mengandung seo dan banyak mengandung kata dari {kata_cleaned} "
                        "tanpa di bold dan anti duplikasi sebanyak 1000 kata,\n"
                    )

                    # Menulis hasil ke dalam hasil.txt
                    f_output.write(article_template)
                else:
                    print("Baris kosong ditemukan di kata.txt, melewati baris ini.")
        print("Hasil Genereta telah disimpan di hasil.txt.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menulis ke hasil.txt: {e}")
