// script.js
(function () {
  const displayEl = document.getElementById('display');
  const incBtn = document.getElementById('increment');
  const decBtn = document.getElementById('decrement');
  const resetBtn = document.getElementById('reset');
  const stepInput = document.getElementById('step');

  // parse and keep value as integer
  let value = 0;
  function render() {
    displayEl.textContent = String(value);
  }

  function getStep() {
    const n = parseInt(stepInput.value, 10);
    return Number.isFinite(n) && n > 0 ? n : 1;
  }

  incBtn.addEventListener('click', () => {
    value += getStep();
    render();
  });

  decBtn.addEventListener('click', () => {
    value -= getStep();
    render();
  });

  resetBtn.addEventListener('click', () => {
    value = 0;
    render();
  });

  // keyboard support
  window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowUp') {
      value += getStep();
      render();
      e.preventDefault();
    }
  });

  // Live-edit step with validation
  stepInput.addEventListener('input', () => {
    // Ensure value is positive integer (display does not change)
    let v = stepInput.value;
    // remove non-digit chars
    v = v.replace(/[^\d]/g, '');
    if (!v) v = '1';
    stepInput.value = v;
  });

  // initial render
  render();
})();
