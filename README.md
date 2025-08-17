
# Custom Wallet Generator

An Ethereum wallet generation tool with custom suffix addresses using multi-processing for optimal performance.

## 🚀 Features

- **Multi-processing**: Uses multiple processes to accelerate search speed
- **Suffix search**: Find wallets with addresses ending in desired strings
- **Real-time statistics**: Display number of wallets created and generation rate
- **Auto-save**: Save results to file when suitable wallet is found
- **Performance optimization**: Automatically adjust number of processes based on CPU

## 📋 System Requirements

### Python Dependencies
```bash
pip install eth-account
```

### System Requirements
- Python 3.7+
- RAM: Minimum 4GB (recommended 8GB+)
- CPU: Multi-core (more cores = faster)

## 🛠️ Installation

1. Clone repository:
```bash
git clone https://github.com/tdat05gj/customwallet.git
cd customwallet
```

2. Install dependencies:
```bash
pip install eth-account
```

## 💻 Usage

### Run the program
```bash
python 1.py
```

### Customize suffix
Open file `1.py` and change the `target_suffix` variable:
```python
target_suffix = "999999999"  # Change to your desired suffix here
```

### Popular suffix examples
- `"999999999"` - 9 consecutive 9s
- `"000000000"` - 9 consecutive 0s  
- `"111111111"` - 9 consecutive 1s
- `"abc123def"` - Custom string

## 📊 Performance

- **Speed**: ~50,000-200,000 wallets/second (depends on CPU)
- **Search time**: Depends on suffix difficulty
- **RAM usage**: ~100-500MB
- **CPU**: Uses 100% of all cores

### Performance by CPU Type
| CPU Type | Cores/Threads | Estimated Speed | 6-char Suffix | 7-char Suffix | 8-char Suffix | 9-char Suffix |
|----------|---------------|----------------|---------------|---------------|---------------|---------------|
| Intel i3-10100 | 4C/8T | ~60,000/s | 1-5 minutes | 10-60 minutes | 3-18 hours | 2-12 days |
| Intel i5-12400 | 6C/12T | ~90,000/s | 30s-3 minutes | 7-40 minutes | 2-12 hours | 1-8 days |
| Intel i7-12700 | 12C/20T | ~140,000/s | 20s-2 minutes | 5-25 minutes | 1-8 hours | 16h-5 days |
| Intel i9-12900K | 16C/24T | ~180,000/s | 15s-90s | 3-20 minutes | 1-6 hours | 12h-4 days |
| AMD Ryzen 5 5600X | 6C/12T | ~85,000/s | 30s-3 minutes | 7-45 minutes | 2-13 hours | 1-9 days |
| AMD Ryzen 7 5800X | 8C/16T | ~120,000/s | 25s-2.5 minutes | 5-30 minutes | 1.5-9 hours | 18h-6 days |
| AMD Ryzen 9 5900X | 12C/24T | ~160,000/s | 20s-2 minutes | 4-22 minutes | 1-7 hours | 14h-4.5 days |
| AMD Ryzen 9 5950X | 16C/32T | ~200,000/s | 15s-80s | 3-18 minutes | 50m-5 hours | 10h-3.5 days |

### Difficulty Estimation (Average CPU)
| Suffix Length | Estimated Time | Attempts Required |
|---------------|----------------|-------------------|
| 4 characters | Few seconds | ~65,000 |
| 5 characters | Few seconds - 1 minute | ~1,000,000 |
| 6 characters | 30s - 5 minutes | ~16,000,000 |
| 7 characters | 5-45 minutes | ~270,000,000 |
| 8 characters | 1-15 hours | ~4,300,000,000 |
| 9 characters | 12h-10 days | ~68,000,000,000 |

## 📁 Output

When a suitable wallet is found, the program will:

1. Display information on console
2. Save to `gj.txt` file with format:
```
Address: 0x1234...999999999
Private Key: 0xabc123...
Attempts: 1,234,567
Time taken: 123.45 seconds
Found by Worker: 5
```

## ⚠️ Security Warning

- **NEVER** share your private key
- Backup private key securely
- Delete `gj.txt` file after use

## 🔧 Advanced Customization

### Change number of processes
```python
generator = FastWalletGenerator(target_suffix, num_processes=16)
```

### Change reporting frequency
In the `generate_wallet_worker` function, change:
```python
if attempts % 10000 == 0:  # Report every 10,000 attempts
```

## 🐛 Troubleshooting

### Missing module error
```bash
pip install eth-account
```

### Slow performance
- Reduce number of processes if RAM is insufficient
- Ensure no other heavy applications are running

### Wallet not found
- Suffix too difficult: try shorter suffix
- Long search time: may need to wait longer

## 📈 Performance Optimization

1. **CPU**: Use CPU with many cores
2. **RAM**: Minimum 8GB to run multiple processes
3. **SSD**: Helps write files faster
4. **Cooling**: Ensure good cooling for long-term operation

### 🖥️ VPS Rental Suggestion for High Performance

If your personal computer is not powerful enough, you can rent a VPS with high configuration:

**Trusted VPS Provider**: [VinaHost](https://secure.vinahost.vn/ac/aff.php?aff=3103) - [Datamart](https://www.databasemart.com/?aff_id=e2e55c86959b4d278a38c59bb2070cd2) - [MTDVPS](https://mtdvps.com/ref/13664)

**Recommended FlexProVPS Custom Configuration**:
- **CPU**: 15+ cores (recommended 20-32 cores)
- **RAM**: 6-12GB
- **Storage**: SSD NVMe
- **OS**: Windows Server 2022

**VPS Performance Estimation**:
| Configuration | Cores | Estimated Speed | 8-char Suffix | 9-char Suffix |
|---------------|-------|----------------|---------------|---------------|
| 15 cores | 15C/30T | ~250,000/s | 30m-3 hours | 6h-2.5 days |
| 20 cores | 20C/40T | ~320,000/s | 20m-2 hours | 4h-2 days |
| 32 cores | 32C/64T | ~500,000/s | 15m-90m | 2.5h-1.5 days |

**VPS Benefits**:
- ✅ Run 24/7 without worrying about shutdown
- ✅ Powerful CPU with many cores
- ✅ High and stable bandwidth
- ✅ No impact on personal computer
- ✅ Reasonable cost for high performance

## 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## 📄 License

This project is for educational and research purposes only.

## ⭐ Support

If this project is helpful, please give it a star! ⭐

---

**Note**: Generating wallets with specific suffixes can take a lot of time and resources. Please consider carefully before running with difficult suffixes.
