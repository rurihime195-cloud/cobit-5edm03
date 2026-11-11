import streamlit as st

st.set_page_config(
    page_title="Evaluasi COBIT 5 EDM03",
    page_icon="📊",
    layout="centered"
)

st.title("Evaluasi COBIT 5 - EDM03")
st.subheader("Ensure Risk Optimisation")

st.write(
    "Aplikasi sederhana untuk melakukan simulasi "
    "penilaian indikator tata kelola risiko TI."
)

indikator = {
    "EDM03.01 - Evaluate Risk Management": [
        "Organisasi mengidentifikasi risiko teknologi informasi.",
        "Organisasi menganalisis dampak risiko TI.",
        "Organisasi menentukan toleransi risiko TI."
    ],
    "EDM03.02 - Direct Risk Management": [
        "Organisasi menetapkan arahan pengelolaan risiko TI.",
        "Organisasi menetapkan tanggung jawab pengelolaan risiko.",
        "Organisasi memastikan tindakan penanganan risiko dilakukan."
    ],
    "EDM03.03 - Monitor Risk Management": [
        "Organisasi memantau perubahan risiko TI.",
        "Organisasi mengevaluasi efektivitas penanganan risiko.",
        "Organisasi melaporkan kondisi risiko TI secara berkala."
    ]
}

kategori = {
    "N": "Not Achieved",
    "P": "Partially Achieved",
    "L": "Largely Achieved",
    "F": "Fully Achieved"
}

st.info("Pilih kategori penilaian untuk setiap indikator.")

hasil = {}

for proses, daftar_indikator in indikator.items():
    st.header(proses)

    for nomor, pertanyaan in enumerate(daftar_indikator, start=1):
        jawaban = st.selectbox(
            pertanyaan,
            options=list(kategori.keys()),
            format_func=lambda x: f"{x} - {kategori[x]}",
            key=f"{proses}_{nomor}"
        )

        hasil.setdefault(proses, []).append(jawaban)

if st.button("Proses Penilaian"):
    st.header("Hasil Penilaian")

    for proses, jawaban in hasil.items():
        st.subheader(proses)

        for kode, nama in kategori.items():
            jumlah = jawaban.count(kode)
            persentase = (jumlah / len(jawaban)) * 100

            st.write(
                f"{nama}: {jumlah} indikator "
                f"({persentase:.1f}%)"
            )

    st.success("Penilaian berhasil diproses!")

    st.caption(
        "Catatan: Hasil ini merupakan rekap simulasi "
        "indikator, bukan penetapan resmi capability level COBIT 5."
    )
