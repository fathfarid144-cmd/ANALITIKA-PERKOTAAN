"""Unduh jaringan jalan kaki seluruh Kota Bandar Lampung dari OpenStreetMap (Overpass API).

Dijalankan sekali untuk menghasilkan data/raw/jalan_bdl_osm_walk.graphml, agar notebook
dapat dijalankan ulang (Restart Kernel and Run All) tanpa internet.

Cara pakai (dari folder data/skrip, di environment conda analitika-perkotaan):
    python unduh_jalan_osm.py

Dokumentasi perolehan data:
- Sumber  : OpenStreetMap contributors (lisensi ODbL), melalui Overpass API memakai osmnx.
- Cakupan : poligon seluruh kelurahan Kota Bandar Lampung + penyangga 1.500 m
            (agar kelurahan tepi kota tetap punya jalan sampai batas).
- Moda    : network_type="walk" (jalan kaki), retain_all=True (komponen terpisah dibuang di notebook).
- Diunduh : 16 November 2026 (36.922 simpul, 92.300 ruas).
"""
from pathlib import Path

import geopandas as gpd
import osmnx as ox

RAW = Path(__file__).resolve().parents[1] / "raw"
CRS_UTM, CRS_GEO = 32748, 4326

kel = gpd.read_file(RAW / "batas_kelurahan_bdl.geojson").to_crs(CRS_UTM)
poligon = gpd.GeoSeries([kel.union_all().buffer(1500).simplify(100)], crs=CRS_UTM).to_crs(CRS_GEO).iloc[0]

ox.settings.requests_timeout = 300
ox.settings.max_query_area_size = 50 * 1000 * 50 * 1000

# Server Overpass publik kadang penuh; coba beberapa peladen secara berurutan.
for url in ["https://overpass-api.de/api", "https://overpass.kumi.systems/api"]:
    ox.settings.overpass_url = url
    try:
        G = ox.graph_from_polygon(poligon, network_type="walk", simplify=True, retain_all=True)
        ox.save_graphml(G, RAW / "jalan_bdl_osm_walk.graphml")
        print(f"OK dari {url}: {len(G)} simpul, {G.number_of_edges()} ruas")
        break
    except Exception as e:  # noqa: BLE001
        print("Gagal dari", url, "->", type(e).__name__, str(e)[:120])
else:
    raise SystemExit("Semua peladen Overpass gagal; coba lagi beberapa menit kemudian.")
