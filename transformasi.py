import math                              # Modul standar untuk fungsi trigonometri (sin, cos) dan konversi radian.
import numpy as np                       # NumPy: operasi matriks/vektor dan tipe array numerik.

# ============================================================================
# KONFIGURASI — EDIT DI SINI
# ============================================================================
UX, UY, UZ        = 2.0, 0.0, 2.0       # Titik u_P pada frame U (koordinat 3D). Ganti ini untuk kasus berbeda.
ALPHA, BETA, GAMMA = 0.0, 0.0, -180     # Sudut Euler ZYX (roll=X, pitch=Y, yaw=Z) dalam DERAJAT.
TX, TY, TZ        = 0.0, 0.0, 0.0       # Vektor translasi dari U ke B (meter).

PRINT_STEPS = True                       # Jika True: cetak matriks antara (Trans, Rz, Ry, Rx) untuk transparansi perhitungan.
# ============================================================================


# -------------------- Pembentuk Matriks Homogen 4×4 --------------------
def Rx_deg(alpha_deg: float) -> np.ndarray:       # Definisi fungsi rotasi sekitar sumbu X (roll) dalam derajat → matriks 4×4.
    """Rotasi roll (X) dalam derajat sebagai matriks homogen 4×4."""
    a = math.radians(alpha_deg)                   # Konversi α derajat → radian (karena sin/cos menerima radian).
    ca, sa = math.cos(a), math.sin(a)             # Hitung cos α dan sin α sekali agar efisien.
    return np.array([                             # Bentuk matriks homogen 4×4 untuk Rx(α).
        [1,  0,   0, 0],
        [0, ca, -sa, 0],
        [0, sa,  ca, 0],
        [0,  0,   0, 1],
    ], dtype=float)

def Ry_deg(beta_deg: float) -> np.ndarray:        # Rotasi sekitar sumbu Y (pitch) dalam derajat → matriks 4×4.
    """Rotasi pitch (Y) dalam derajat sebagai matriks homogen 4×4."""
    b = math.radians(beta_deg)                    # Konversi β ke radian.
    cb, sb = math.cos(b), math.sin(b)             # cos β dan sin β.
    return np.array([                             # Matriks homogen 4×4 untuk Ry(β).
        [ cb, 0, sb, 0],
        [  0, 1,  0, 0],
        [-sb, 0, cb, 0],
        [  0, 0,  0, 1],
    ], dtype=float)

def Rz_deg(gamma_deg: float) -> np.ndarray:       # Rotasi sekitar sumbu Z (yaw) dalam derajat → matriks 4×4.
    """Rotasi yaw (Z) dalam derajat sebagai matriks homogen 4×4."""
    g = math.radians(gamma_deg)                   # Konversi γ ke radian.
    cg, sg = math.cos(g), math.sin(g)             # cos γ dan sin γ.
    return np.array([                             # Matriks homogen 4×4 untuk Rz(γ).
        [cg, -sg, 0, 0],
        [sg,  cg, 0, 0],
        [ 0,   0, 1, 0],
        [ 0,   0, 0, 1],
    ], dtype=float)

def Trans(tx: float, ty: float, tz: float) -> np.ndarray:  # Translasi (tx, ty, tz) → matriks homogen 4×4.
    """Translasi sebagai matriks homogen 4×4."""
    T = np.eye(4, dtype=float)                   # Mulai dari matriks identitas 4×4.
    T[:3, 3] = [tx, ty, tz]                      # Masukkan vektor translasi ke kolom ke-4 (indeks 3) baris 0..2.
    return T                                     # Baris terakhir tetap [0,0,0,1] sesuai definisi homogen.

def build_T_zyx(alpha_deg: float, beta_deg: float, gamma_deg: float,
                tx: float, ty: float, tz: float) -> np.ndarray:
    """
    Susun transform homogen sesuai teori (ZYX):
      T = Trans(t) @ Rz(gamma) @ Ry(beta) @ Rx(alpha)
    """
    Tt  = Trans(tx, ty, tz)                      # Bangun matriks translasi Tt.
    Rz  = Rz_deg(gamma_deg)                      # Bangun matriks rotasi yaw Rz(γ).
    Ry  = Ry_deg(beta_deg)                       # Bangun matriks rotasi pitch Ry(β).
    Rx  = Rx_deg(alpha_deg)                      # Bangun matriks rotasi roll Rx(α).
    T   = Tt @ Rz @ Ry @ Rx                      # PERKALIAN MATRIKS 4×4: urutan penting (kanan → kiri diterapkan ke vektor).
    if PRINT_STEPS:                              # Jika ingin melihat komponen penyusunnya:
        print_matrix("Trans(t)", Tt)             # Cetak Tt
        print_matrix("Rz(gamma)", Rz)            # Cetak Rz
        print_matrix("Ry(beta)", Ry)             # Cetak Ry
        print_matrix("Rx(alpha)", Rx)            # Cetak Rx
    return T                                     # Kembalikan T total.

# -------------------- Utilitas Koordinat Homogen --------------------
def to_h(p3: tuple[float, float, float]) -> np.ndarray:
    """(x,y,z) → (x,y,z,1)^T"""
    return np.array([p3[0], p3[1], p3[2], 1.0], dtype=float)  # Tambahkan 1 di komponen w agar bisa dikali T (4×4).

def from_h(p4: np.ndarray) -> np.ndarray:
    """(x,y,z,w)^T → (x,y,z) (asumsi w ≈ 1)"""
    w = p4[3] if p4[3] != 0 else 1.0            # Ambil w; kalau nol (kasus langka), pakai 1 untuk hindari bagi 0.
    return p4[:3] / w                           # Kembalikan ke koordinat Kartesius 3D: (x/w, y/w, z/w).

def apply_T(T: np.ndarray, pU3: tuple[float, float, float]) -> np.ndarray:
    """p_B = T @ p_U (koordinat homogen)."""
    return from_h(T @ to_h(pU3))                # Ubah pU → homogen, kalikan T, lalu kembali ke 3D.

# -------------------- Utility Cetak --------------------
def print_matrix(label: str, M: np.ndarray) -> None:
    np.set_printoptions(suppress=True, floatmode="maxprec_equal", linewidth=100)
    print(f"{label} =\n{M}\n")                  # Cetak matriks dengan opsi tampilan numerik rapi.

# -------------------- Main --------------------
if __name__ == "__main__":                      # Guard standar Python: blok ini hanya jalan saat file dieksekusi langsung.
    # Bangun T sesuai konfigurasi
    T = build_T_zyx(ALPHA, BETA, GAMMA, TX, TY, TZ)    # Bangun matriks transform total T dari α,β,γ dan t.
    print_matrix("T (Trans @ Rz @ Ry @ Rx)", T)        # Tampilkan T agar kita bisa verifikasi secara visual.

    # Transform titik u_P → b_P
    pU = (UX, UY, UZ)                                   # Ambil titik asal u_P dari konfigurasi.
    pB = apply_T(T, pU)                                 # Hitung b_P = T * u_P (homogen).

    print(f"u_P = {pU}")                                # Cetak titik asal untuk referensi.
    print(f"b_P = {pB}")                                # Cetak hasil transformasi pada frame B.
