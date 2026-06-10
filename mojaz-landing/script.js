document.addEventListener('DOMContentLoaded', () => {
  const pointsEl = document.querySelector('.mazeed__points-num');
  const redeemButtons = document.querySelectorAll('.store-card:not(.store-card--locked) .btn--primary');

  redeemButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
      const card = btn.closest('.store-card');
      const priceText = card.querySelector('.price').textContent.replace(/[^\d]/g, '');
      const price = Number(priceText);
      const current = Number(pointsEl.textContent.replace(/,/g, ''));

      if (current < price) {
        btn.textContent = 'نقاط غير كافية';
        btn.disabled = true;
        setTimeout(() => {
          btn.textContent = 'استبدال';
          btn.disabled = false;
        }, 1500);
        return;
      }

      pointsEl.textContent = (current - price).toLocaleString('en-US');
      btn.textContent = 'تم الاستبدال ✓';
      btn.disabled = true;
    });
  });

  const reportBtn = document.querySelector('.report-card__actions .btn--primary');
  const reportInput = document.querySelector('.report-card__input');
  if (reportBtn && reportInput) {
    reportBtn.addEventListener('click', () => {
      if (!reportInput.value.trim()) {
        reportInput.style.borderColor = '#d6193c';
        reportInput.placeholder = 'الرجاء إدخال رقم الهيكل أو الرقم التسلسلي';
      }
    });
    reportInput.addEventListener('input', () => {
      reportInput.style.borderColor = '';
    });
  }
});
