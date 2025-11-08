(function(){
    const fish = document.querySelector('.fish');
    const container = document.querySelector('.bubbles');
    if(!fish || !container) return;

    const SPAWN_INTERVAL = 1000; // ms
    const MAX_BUBBLES = 60;

    function spawnBubble(){
      if(container.children.length > MAX_BUBBLES){
        container.removeChild(container.firstElementChild);
      }

      const rect = fish.getBoundingClientRect();
      const scrollX = window.scrollX || window.pageXOffset;
      const scrollY = window.scrollY || window.pageYOffset;

      const startX = scrollX + rect.left + rect.width * 0.55 + (Math.random() - 0.5) * rect.width * 0.6;
      const startY = scrollY + rect.top + rect.height * 0.5 + (Math.random() - 0.5) * rect.height * 0.2;

      const bubble = document.createElement('span');
      bubble.className = 'bubble';

      const size = 8 + Math.random() * 20;                 // 8px..28px
      const duration = 6 + Math.random() * 6;             // 6s..12s (rise duration)
      const drift = (Math.random() * 160 - 80) + 'px';    // -80px..+80px horizontal drift

      bubble.style.left = startX + 'px';
      bubble.style.top  = startY + 'px';
      bubble.style.setProperty('--size', size + 'px');
      bubble.style.setProperty('--duration', duration + 's');
      bubble.style.setProperty('--drift', drift);

      container.appendChild(bubble);

      // schedule pop at a random height (not a random time)
      // CSS translates bubbles by -200vh (see rise keyframes), so total travel = 2 * innerHeight
      const travelPx = window.innerHeight * 2;
      const minOffset = Math.max(30, size); // avoid immediate pop
      const popOffset = minOffset + Math.random() * Math.max(0, travelPx - minOffset);
      const timeToPopMs = duration * (popOffset / travelPx) * 1000;

      const popTimeout = setTimeout(() => {
        if (!bubble || !bubble.parentNode) return;
        bubble.classList.add('pop');
        setTimeout(() => { if (bubble && bubble.parentNode) bubble.remove(); }, 320);
      }, timeToPopMs);

      // interaction: pop on pointerdown / pointerenter
      const doPop = () => {
        if (!bubble || bubble.classList.contains('pop')) return;
        clearTimeout(popTimeout);
        bubble.classList.add('pop');
        setTimeout(() => { if (bubble && bubble.parentNode) bubble.remove(); }, 320);
      };
      bubble.addEventListener('pointerdown', doPop, { passive: true });
      bubble.addEventListener('pointerenter', doPop, { passive: true });

      // cleanup if animation reaches the end
      bubble.addEventListener('animationend', (e) => {
        if (e.animationName === 'rise') {
          clearTimeout(popTimeout);
          if (bubble && bubble.parentNode) bubble.remove();
        }
      }, { once: true });
    }

    const intervalId = setInterval(spawnBubble, SPAWN_INTERVAL);

    // stop generation when page hidden
    document.addEventListener('visibilitychange', () => {
      if(document.hidden) clearInterval(intervalId);
    });
  })();