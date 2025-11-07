Metodika:

1. Har backend uchun 100 ta ketma-ket save operatsiyasini o'lchash; har bir operatsiya `time.perf_counter()` orqali o'lchanadi.
2. Statistikalar: min, median, mean, max, stdev, p95, p99.
3. Test muhiti: lokal (SSD/HDD), tarmoq sharoiti (S3 uchun region, internet tezligi).

Mock natijalar (misol, siz o'zingiz sinab ko'ring):

1. MockS3 (in-memory): mean ~ 0.0005–0.01s, median juda kichik.
2. Local filesystem (SSD, 1KB fayl): mean ~ 0.001–0.005s.
3. Real S3 (1KB fayl, internetga bog'liq): mean ~ 0.05–0.3s, p99 ba'zan 0.5–1.0s bo'lishi mumkin (region va routingga qarab).

Reliability muammolari:

1. Tarmoq xatolari va S3 5xx javoblar.
2. Credential yoki permission xatolari.
3. Idempotency: `put_object` odatda idempotent emas, lekin fayl bir xil key bilan qayta yuklanishi mumkin; performans/atomicity haqida o'ylash kerak.

   Strategiyalar:
4. Retry bilan exponential backoff va jitter.
5. Circuit breaker pattern.
6. Background queue (local -> queued -> push to S3) — offline-first variant.
7. Multipart upload katta fayllar uchun.

   Testlar:
8. Moklar orqali 5xx xatolarni simulyatsiya qilib retryni tekshirish.
9. Stress testlar parallel so'rovlarni yuborish va p95/p99 ni ko'rish.

Recomendatsiyalar:

1. CI da AWS credential ishlatmang; `moto` yoki Mock adapter ishlating.
2. Production uchun `tenacity` (retry), `aioboto3` yoki asinxron client va multipart upload qollanilsin.
3. Katta fayllar uchun streaming va chunk-based uploads ishlating.
