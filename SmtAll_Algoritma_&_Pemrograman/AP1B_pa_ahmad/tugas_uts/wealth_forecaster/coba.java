@Service
public class WalletService {

    // Memastikan jika terjadi error, uang batal dipotong (Transaksi di-rollback)
    @Transactional
    public TransactionResponse executeTransfer(TransferRequest request) {
        String key = request.getIdempotencyKey();

        // Langkah 1: Mencegah tombol bayar tertekan dua kali (Idempotency)
        if (transactionLogRepository.existsById(key)) {
            return throwDuplicateWarning(key);
        }

        // Langkah 2: Menggembok data dompet pelanggan secara fisik di sistem
        Wallet senderWallet = walletRepository.findAndLockByUserId(request.getSenderId())
                .orElseThrow(() -> new UserNotFoundException());

        // Langkah 3: Validasi kecukupan saldo
        if (senderWallet.getBalance().compareTo(request.getAmount()) < 0) {
            throw new InsufficientBalanceException("Saldo tidak cukup");
        }

        // Langkah 4: Pemotongan saldo dan penyimpanan
        senderWallet.setBalance(senderWallet.getBalance().subtract(request.getAmount()));
        walletRepository.save(senderWallet);

        return new TransactionResponse("SUCCESS");
    }
}