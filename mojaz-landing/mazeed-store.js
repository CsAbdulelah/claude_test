document.addEventListener('DOMContentLoaded', () => {
  // Category chips
  const chips = document.querySelectorAll('.chip');
  chips.forEach((chip) => {
    chip.addEventListener('click', () => {
      chips.forEach((c) => c.classList.remove('chip--active'));
      chip.classList.add('chip--active');
    });
  });

  // Favorite toggle
  document.querySelectorAll('.fav-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      btn.classList.toggle('fav-btn--active');
      btn.textContent = btn.classList.contains('fav-btn--active') ? '♥' : '♡';
    });
  });

  // Add to cart
  const cartCount = document.querySelector('.cart-bar__count');
  let count = 0;
  document.querySelectorAll('.product-card .btn--primary').forEach((btn) => {
    btn.addEventListener('click', () => {
      count += 1;
      cartCount.textContent = count;
      btn.textContent = 'تمت الإضافة ✓';
      setTimeout(() => { btn.textContent = 'أضف للسلة'; }, 1200);
    });
  });

  // Load more (demo)
  const loadMore = document.querySelector('.load-more');
  if (loadMore) {
    loadMore.addEventListener('click', () => {
      loadMore.textContent = 'جارِ التحميل...';
      setTimeout(() => { loadMore.textContent = 'لا مزيد من المنتجات'; loadMore.disabled = true; }, 800);
    });
  }
});
