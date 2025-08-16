import os
import secrets
import multiprocessing as mp
from multiprocessing import Queue, Process
import time
from eth_account import Account
from threading import Thread
import queue

class FastWalletGenerator:
    def __init__(self, target_suffix="999999999", num_processes=None):
        self.target_suffix = target_suffix.lower()
        # Tối ưu cho 18-core: dùng 36 processes (2x cores)
        self.num_processes = num_processes or min(os.cpu_count() * 2, 36)
        self.found_queue = Queue()
        self.stats_queue = Queue()
        self.total_attempts = 0
        
    def generate_wallet_worker(self, worker_id, result_queue, stats_queue):
        """Worker process để tạo ví"""
        attempts = 0
        start_time = time.time()
        
        while True:
            # Tạo khóa riêng tư ngẫu nhiên
            private_key = "0x" + secrets.token_hex(32)
            account = Account.from_key(private_key)
            address = account.address.lower()
            
            attempts += 1
            
            # Báo cáo tiến trình mỗi 10000 lần thử
            if attempts % 10000 == 0:
                elapsed = time.time() - start_time
                rate = attempts / elapsed if elapsed > 0 else 0
                stats_queue.put((worker_id, attempts, rate))
            
            # Kiểm tra suffix
            if address.endswith(self.target_suffix):
                # Tạo mnemonic (seed phrase) - đơn giản hóa
                result = {
                    'address': account.address,
                    'private_key': private_key,
                    'worker_id': worker_id,
                    'attempts': attempts,
                    'time_taken': time.time() - start_time
                }
                result_queue.put(result)
                break
                
    def stats_monitor(self):
        """Monitor thống kê từ các worker"""
        total_attempts = 0
        worker_stats = {}
        
        while True:
            try:
                worker_id, attempts, rate = self.stats_queue.get(timeout=1)
                worker_stats[worker_id] = (attempts, rate)
                
                # Tính tổng attempts
                total_attempts = sum(stats[0] for stats in worker_stats.values())
                
                print(f"Wallets created: {total_attempts:,}")
                
            except queue.Empty:
                continue
            except:
                break
                
    def generate(self):
        """Tạo ví với multi-processing"""
        print(f"Starting wallet generation with {self.num_processes} processes...")
        print(f"Target suffix: {self.target_suffix}")
        print("")
        
        # Tạo processes
        processes = []
        for i in range(self.num_processes):
            p = Process(target=self.generate_wallet_worker, 
                       args=(i, self.found_queue, self.stats_queue))
            p.start()
            processes.append(p)
            
        # Tạo thread monitor thống kê
        stats_thread = Thread(target=self.stats_monitor, daemon=True)
        stats_thread.start()
        
        try:
            # Chờ kết quả
            result = self.found_queue.get()
            
            # Dừng tất cả processes
            for p in processes:
                p.terminate()
                p.join()
                
            # In kết quả
            print(f"\n\n🎉 FOUND WALLET! 🎉")
            print(f"Address: {result['address']}")
            print(f"Private Key: {result['private_key']}")
            print(f"Found by Worker: {result['worker_id']}")
            print(f"Attempts: {result['attempts']:,}")
            print(f"Time taken: {result['time_taken']:.2f} seconds")
            
            # Lưu vào file
            with open("gj.txt", "w") as f:
                f.write(f"Address: {result['address']}\n")
                f.write(f"Private Key: {result['private_key']}\n")
                f.write(f"Attempts: {result['attempts']:,}\n")
                f.write(f"Time taken: {result['time_taken']:.2f} seconds\n")
                f.write(f"Found by Worker: {result['worker_id']}\n")
                
            print("\n✅ Results saved to gj.txt")
            
        except KeyboardInterrupt:
            print("\n\nStopping all processes...")
            for p in processes:
                p.terminate()
                p.join()
            print("Stopped.")

def main():
    # Thay đổi suffix ở đây
    target_suffix = "999999999"
    
    generator = FastWalletGenerator(target_suffix)
    generator.generate()

if __name__ == "__main__":
    main()
