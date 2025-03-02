from ultralytics import YOLO
import os
import argparse
from concurrent.futures import ThreadPoolExecutor

def remove_non_person(image_folder, model, conf):
    print(f"Cleaning {image_folder}")
    # Loop melalui setiap gambar di folder
    for image_name in os.listdir(image_folder):
        # Proses hanya file gambar
        if image_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(image_folder, image_name)
            results = model(image_path, conf=conf)

            # Cek apakah ada orang yang terdeteksi
            person_detected = False
            for result in results:
                for box in result.boxes:
                    if box.cls == 0:  # Class ID 0 untuk 'person' pada dataset COCO
                        person_detected = True
                        break
                if person_detected:
                    break

            # Hapus gambar jika tidak ada orang yang terdeteksi
            if not person_detected:
                os.remove(image_path)
                print(f"Deleted {image_path}")

def main(args):
    # Load model YOLO
    model = YOLO(args.model_path)
    
    if args.multithread:
        # Jika --num_threads tidak diisi, maka default jumlah thread = jumlah folder
        num_threads = args.num_threads if args.num_threads is not None else len(args.image_folders)
        print(f"Running with multithreading enabled. Number of threads: {num_threads}")
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            for folder in args.image_folders:
                futures.append(executor.submit(remove_non_person, folder, model, args.conf))
            # Menunggu semua thread selesai
            for future in futures:
                future.result()
    else:
        # Proses sequential
        for folder in args.image_folders:
            remove_non_person(folder, model, args.conf)
    print("Cleaning completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean images without person detected using YOLO")
    parser.add_argument(
        "--model_path",
        type=str,
        default="best.pt",
        help="Path ke model YOLO yang digunakan (default: best.pt)"
    )
    parser.add_argument(
        "--conf",
        type=float,
        default=0.4,
        help="Confidence threshold untuk deteksi (default: 0.4)"
    )
    parser.add_argument(
        "--image_folders",
        nargs="+",
        required=True,
        help="Daftar folder yang berisi gambar (pisahkan dengan spasi)"
    )
    parser.add_argument(
        "--multithread",
        action="store_true",
        help="Aktifkan multithreading untuk memproses folder secara bersamaan"
    )
    parser.add_argument(
        "--num_threads",
        type=int,
        default=None,
        help="Jumlah thread yang digunakan (default: jumlah folder)"
    )
    args = parser.parse_args()
    main(args)
