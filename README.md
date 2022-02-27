# convex-hull

### deskripsi

program ini merupakan proof of concept divide an conquer, yang ditunjukan dengan menyelesaikan persoalan convex hull.

#### penjelasan convex hull

pada persoalan convex hull, kita diberikan sekumpulan titik dengan lokasinya (misalnya titik dengan nilai x dan y masing-masing mewakili lokasi titik tersebut pada sebuah diagram kartesian), dan target kita adalah menentukan 'titik-titik terluar' dari sekumpulan titik tersebut.
![ilustrasi convex hull](./ConvexHull.png)

### urusan teknis

program ini dibuat dengan python, dan python notebook
beberapa module python yang digunakan adalah

1. numpy `pip install numpy`
2. matplotlib `pip install -U pip` `pip install -U matplotlib`
3. pandas `pip install pandas`
4. scikit learn `pip install -U scikit-learn`

kode install diatas diambil dari website masing-masing module.
if you face any problem while installing, refer to the website for each of those modules.

### cara menjalankan

#### file di src

ada dua file utama di dalam folder src, `myConvexHull.py` dan `main.ipynb`. guna utama file pertama adalah menyimpan fungsi myConvexHull, sedangkan file kedua berisi kode untuk mencoba fungsi myConvexHull.

#### main

buka main.ipynb (dengan menggunakan IDE apapun yang mendukung, misalnya jupyter notebook atau visual studio code). tiap cell 'kotak' dikelompokan untuk menguji satu buah data (dengan total ada enam buah data). untuk mencoba fungsi(yang digunakan pada tiap cell), jalankan cell.

---

dibuat oleh Christopher Jeffrey, NIM 13520055
