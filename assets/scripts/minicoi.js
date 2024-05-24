(({ document: d, navigator: { serviceWorker: s } }) => {
  console.log("minicoi.js loaded");
  if (d) {
      const { currentScript: c } = d;
      console.log("Registering service worker from:", c.src);
      s.register(c.src, { scope: c.getAttribute('scope') || '.' }).then(r => {
          console.log("Service worker registered:", r);
          r.addEventListener('updatefound', () => {
              console.log("Update found, reloading page");
              location.reload();
          });
          if (r.active && !s.controller) {
              console.log("Service worker active, reloading page");
              location.reload();
          }
      }).catch(e => {
          console.error("Service worker registration failed:", e);
      });
  } else {
      addEventListener('install', () => {
          console.log("Service worker installed, skipping waiting");
          skipWaiting();
      });
      addEventListener('activate', e => {
          console.log("Service worker activated, claiming clients");
          e.waitUntil(clients.claim());
      });
      addEventListener('fetch', e => {
          console.log("Fetch event for:", e.request.url);
          const { request: r } = e;
          if (r.cache === 'only-if-cached' && r.mode !== 'same-origin') return;
          e.respondWith(fetch(r).then(r => {
              const { body, status, statusText } = r;
              if (!status || status > 399) return r;
              const h = new Headers(r.headers);
              h.set('Cross-Origin-Opener-Policy', 'same-origin');
              h.set('Cross-Origin-Embedder-Policy', 'require-corp');
              h.set('Cross-Origin-Resource-Policy', 'cross-origin');
              return new Response(body, { status, statusText, headers: h });
          }));
      });
  }
})(self);
