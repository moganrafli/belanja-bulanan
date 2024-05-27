import datetime

def belanja_bulanan():
    daftar_belanja = {}
    total_belanja = 0
    
    while True:
        item = input("Masukkan nama barang : ").lower()
        if item == 'done':
            break
        
        harga = float(input("Masukkan harga barang: "))  
        quantity = int(input("Masukkan jumlah barang: "))  
        
        daftar_belanja[item] = (harga, quantity)  
        total_belanja += harga * quantity  
        
    tanggal_pembelian = datetime.date.today()  
    
    print("\nDaftar Belanja:")
    for item, (harga, quantity) in daftar_belanja.items():  
        print(f"{item.capitalize()}: Rp {harga:,.0f} x {quantity}")  
        
    print(f"\nTotal Belanja: Rp {total_belanja:,.0f}") 
    print(f"Tanggal Pembelian: {tanggal_pembelian.strftime('%d %B %Y')}")  

if __name__ == "__main__":
    print("*****Selamat datang di Program Belanja Bulanan Manggela!***** \n")
    print("Ketik 'done' bila sudah selesai.\n")
    belanja_bulanan()
