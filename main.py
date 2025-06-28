import string
from itertools import product, permutations

# ---- Enigma Tanımları ----

alphabet = string.ascii_uppercase

# 3 adet sabit rotor
rotors = {
    'I':     "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    'II':    "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    'III':   "BDFHJLCPRTXVZNYEIWGAKMUSQO"
}

# Reflector B
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

def rotate(char, offset):
    idx = (alphabet.index(char) + offset) % 26
    return alphabet[idx]

def inverse_rotate(char, offset):
    idx = (alphabet.index(char) - offset) % 26
    return alphabet[idx]

def enigma(text, rotor_names, rotor_positions):
    rotor1, rotor2, rotor3 = [rotors[r] for r in rotor_names]
    pos1, pos2, pos3 = [alphabet.index(p) for p in rotor_positions]
    result = ""

    for char in text:
        if char not in alphabet:
            continue

        # Rotor stepping (yalnızca rotor1 döner)
        pos1 = (pos1 + 1) % 26

        # --- Gidiş ---
        c = rotate(char, pos1)
        c = rotor1[alphabet.index(c)]

        c = rotate(c, pos2 - pos1)
        c = rotor2[alphabet.index(c)]

        c = rotate(c, pos3 - pos2)
        c = rotor3[alphabet.index(c)]

        # Reflector
        c = reflector[alphabet.index(c)]

        # --- Dönüş ---
        c = alphabet[rotor3.index(c)]
        c = inverse_rotate(c, pos3 - pos2)

        c = alphabet[rotor2.index(c)]
        c = inverse_rotate(c, pos2 - pos1)

        c = alphabet[rotor1.index(c)]
        c = inverse_rotate(c, pos1)

        result += c

    return result

# ---- Şifre Kırma (Crib-Based Brute Force) ----

def crack_enigma(ciphertext, crib):
    rotor_orderings = list(permutations(['I', 'II', 'III']))
    positions = product(alphabet, repeat=3)

    for rotor_order in rotor_orderings:
        for pos in positions:
            decrypted = enigma(ciphertext, rotor_order, pos)
            if crib in decrypted:
                print(f"\n[!] EŞLEŞME BULUNDU!")
                print(f"Rotorlar: {rotor_order}, Pozisyonlar: {pos}")
                print(f"Çözülmüş Mesaj: {decrypted}")
                return rotor_order, pos, decrypted

    print("Hiçbir eşleşme bulunamadı.")
    return None

# ---- main() ----

def main():
    print("=== Enigma Şifreleme & Kırma ===\n")

    # Kullanıcıdan açık mesaj alın
    message = "WETTERBERICHTISTGUT"
    print(f"Açık mesaj: {message}")

    # Rotorlar ve pozisyonlar
    rotor_order = ('I', 'II', 'III')
    positions = ('A', 'A', 'A')

    # Şifreleme
    ciphertext = enigma(message, rotor_order, positions)
    print(f"Şifreli mesaj: {ciphertext}")

    # Crib ile brute force çözüm
    crib = "WETTER"
    print(f"\nŞifre çözme başlatılıyor... (crib: '{crib}')")
    crack_enigma(ciphertext, crib)

if __name__ == "__main__":
    main()
