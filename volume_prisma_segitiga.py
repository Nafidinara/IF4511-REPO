def volume_prisma_segitiga(alas, tinggi, tinggi_prisma):
  """
  Menghitung volume prisma segitiga.

  Args:
    alas: Panjang alas segitiga.
    tinggi: Tinggi segitiga.
    tinggi_prisma: Tinggi prisma.

  Returns:
    Volume prisma segitiga.
  """

  luas_alas = alas * tinggi / 2
  return luas_alas * tinggi_prisma


if __name__ == "__main__":
  alas = float(input("Masukkan panjang alas segitiga: "))
  tinggi = float(input("Masukkan tinggi segitiga: "))
  tinggi_prisma = float(input("Masukkan tinggi prisma: "))

  volume = volume_prisma_segitiga(alas, tinggi, tinggi_prisma)
  print("Volume prisma segitiga adalah:", volume)
