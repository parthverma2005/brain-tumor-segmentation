export function initCursorOrbs() {
  const orbs = document.querySelectorAll(".floating-orb");

  document.addEventListener("mousemove", (e) => {
    const { clientX, clientY } = e;

    orbs.forEach((orb, index) => {
      const speed = (index + 1) * 0.02; 
      const x = (window.innerWidth / 2 - clientX) * speed;
      const y = (window.innerHeight / 2 - clientY) * speed;
      orb.style.transform = `translate(${x}px, ${y}px)`;
    });
  });
}
