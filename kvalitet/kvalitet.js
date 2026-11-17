// Kvalitet: sender anonyme hendelser fra simuleringsverktøyene til kvalitetsdelen (Azure, takt-API-et).
// Bruk i et verktøy:
//   <script src="https://seiknes-ui.github.io/simmulator/kvalitet/kvalitet.js" defer></script>
//   window.Kvalitet && Kvalitet.logg('teori', 'feil', { k: id, t: spørsmål, a: valgt svar, m: 'm2.4' });
//
// Det sendes ingen navn eller ID. Hendelser samles i noen sekunder og sendes samlet.
// Feiler sendingen, skjer det ingenting – verktøyet virker som før.
(function () {
  'use strict';
  var URL = 'https://black-coast-081791b1e.1.azurestaticapps.net/api/kvalitet';
  var MAKS = 20, VENT = 4000;
  var ko = [], tid = 0;

  // Ingen innsamling når siden kjøres lokalt fra disk eller inne i claude.ai.
  var av = location.protocol === 'file:' || /claude\.ai$|claudeusercontent\.com$/.test(location.hostname);
  try { if (localStorage.getItem('kvalitet-av') === '1') av = true; } catch (e) {}

  function send() {
    clearTimeout(tid); tid = 0;
    while (ko.length) {
      var del = JSON.stringify(ko.splice(0, MAKS));
      try {
        // text/plain gir en enkel forespørsel uten CORS-forhåndssjekk. Svaret trengs ikke.
        var ok = navigator.sendBeacon && navigator.sendBeacon(URL, new Blob([del], { type: 'text/plain' }));
        if (!ok) fetch(URL, { method: 'POST', mode: 'no-cors', keepalive: true, headers: { 'Content-Type': 'text/plain' }, body: del }).catch(function () {});
      } catch (e) {}
    }
  }

  function logg(verktoy, hendelse, data) {
    if (av) return;
    data = data || {};
    var kort = function (s, n) { return s == null ? '' : String(s).slice(0, n); };
    ko.push({ v: verktoy, h: hendelse, k: kort(data.k, 60), t: kort(data.t, 160), a: kort(data.a, 120), m: kort(data.m, 40) });
    if (ko.length >= MAKS) send();
    else if (!tid) tid = setTimeout(send, VENT);
  }

  // Send det som står i kø når eleven lukker eller bytter fane.
  addEventListener('pagehide', send);
  document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'hidden') send(); });

  window.Kvalitet = { logg: logg, send: send };
})();
