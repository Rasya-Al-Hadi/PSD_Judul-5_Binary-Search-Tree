class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BSTDasar:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_node(root.left, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, key)
        return root

    def insert(self, key):
        self.root = self.insert_node(self.root, key)

    def search_node(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        if key < root.key:
            return self.search_node(root.left, key)
        return self.search_node(root.right, key)

    def search(self, key):
        return self.search_node(self.root, key)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.key, end=" ")
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return
        print(root.key, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.key, end=" ")

    def find_min(self, root):
        if root is None:
            return -1
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    def find_max(self, root):
        if root is None:
            return -1
        current = root
        while current.right is not None:
            current = current.right
        return current.key

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def sum_nodes(self, root):
        if root is None:
            return 0
        return root.key + self.sum_nodes(root.left) + self.sum_nodes(root.right)


def main():
    perpustakaan = BSTDasar()
    pilih = 0

    while pilih != 10:
        print("\n===SISTEM DATA NOMOR RAK PERPUSTAKAAN===")
        print("1. Tambah Nomor Rak")
        print("2. Cari Nomor Rak")
        print("3. Tampilkan Rak (Urut Naik)")
        print("4. Tampilkan Rak (Preorder)")
        print("5. Tampilkan Rak (Postorder)")
        print("6. Nomor Rak Terkecil")
        print("7. Nomor Rak Terbesar")
        print("8. Jumlah Rak Terdaftar")
        print("9. Total Seluruh Nomor Rak")
        print("10. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                x = int(input("Masukkan nomor rak: "))
                perpustakaan.insert(x)
                print(f"Nomor rak {x} berhasil ditambahkan.")
            except ValueError:
                print("Nomor rak harus berupa angka!")
        elif pilih == 2:
            try:
                x = int(input("Masukkan nomor rak yang dicari: "))
                if perpustakaan.search(x):
                    print("Nomor rak ditemukan")
                else:
                    print("Nomor rak tidak ditemukan")
            except ValueError:
                print("Input haeus berupa angka!")
        elif pilih == 3:
            print("Daftar nomor rak (urut naik): ", end="")
            perpustakaan.inorder(perpustakaan.root)
            print()
        elif pilih == 4:
            print("Nomor rak (Preorder): ", end="")
            perpustakaan.preorder(perpustakaan.root)
            print()
        elif pilih == 5:
            print("Tampilkan Rak (Postorder): ", end="")
            perpustakaan.postorder(perpustakaan.root)
            print()
        elif pilih == 6:
            print(f"Nomor Rak Terkecil: {perpustakaan.find_min(perpustakaan.root)}")
        elif pilih == 7:
            print(f"Nomor Rak Terbesar: {perpustakaan.find_max(perpustakaan.root)}")
        elif pilih == 8:
            print(f"Jumlah Rak Terdaftar: {perpustakaan.count_nodes(perpustakaan.root)}")
        elif pilih == 9:
            print(f"Total Seluruh Nomor Rak: {perpustakaan.sum_nodes(perpustakaan.root)}")
        elif pilih == 10:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()