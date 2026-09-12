
(function(){
  "use strict";
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var yr = document.getElementById('yr');
  if(yr) yr.textContent = new Date().getFullYear();

  /* ---------- hero entrance ---------- */
  var hero = document.getElementById('hero');
  if(hero) requestAnimationFrame(function(){ setTimeout(function(){ hero.classList.add('is-lit'); }, 90); });

  /* ---------- generic reveals ---------- */
  var io = new IntersectionObserver(function(es){
    es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('is-in'); io.unobserve(e.target); } });
  }, { threshold:.14, rootMargin:'0px 0px -8% 0px' });
  document.querySelectorAll('[data-reveal],[data-proj],[data-why],[data-fig]').forEach(function(el){ io.observe(el); });

  /* ---------- nav: stuck state + scroll spy + indicator ---------- */
  var nav = document.getElementById('nav');
  var links = Array.prototype.slice.call(document.querySelectorAll('.nav-link'));
  var ind = document.getElementById('navInd');

  function onScroll(){ nav.classList.toggle('is-stuck', window.scrollY > 24); }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive:true });

  function moveInd(link){
    if(!link){ ind.classList.remove('on'); return; }
    ind.style.width = link.offsetWidth + 'px';
    ind.style.transform = 'translateX(' + link.offsetLeft + 'px)';
    ind.classList.add('on');
  }
  var spy = new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(!e.isIntersecting) return;
      var id = e.target.id;
      var active = null;
      links.forEach(function(l){
        var on = l.getAttribute('href') === '#' + id;
        l.classList.toggle('is-active', on);
        if(on) active = l;
      });
      moveInd(active);
    });
  }, { threshold:.01, rootMargin:'-45% 0px -50% 0px' });
  ['services','work','expertise','about','contact'].forEach(function(id){
    var s = document.getElementById(id); if(s) spy.observe(s);
  });
  window.addEventListener('resize', function(){
    var a = document.querySelector('.nav-link.is-active'); if(a) moveInd(a);
  });

  /* ---------- mobile menu ---------- */
  var burger = document.getElementById('burger');
  var menu = document.getElementById('menu');
  function setMenu(open){
    document.body.classList.toggle('menu-open', open);
    burger.setAttribute('aria-expanded', String(open));
    burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    document.body.style.overflow = open ? 'hidden' : '';
    Array.prototype.forEach.call(menu.querySelectorAll('.menu-link'), function(l,i){
      l.style.transitionDelay = open ? (0.12 + i*0.06) + 's' : '0s';
    });
  }
  burger.addEventListener('click', function(){ setMenu(!document.body.classList.contains('menu-open')); });
  menu.addEventListener('click', function(e){ if(e.target.closest('a')) setMenu(false); });
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape') setMenu(false); });

  /* ---------- count up ---------- */
  var cio = new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(!e.isIntersecting) return;
      var el = e.target, to = parseInt(el.dataset.count,10), t0 = null, dur = 1400;
      if(reduce){ el.textContent = to; cio.unobserve(el); return; }
      function tick(t){
        if(!t0) t0 = t;
        var p = Math.min((t - t0)/dur, 1);
        el.textContent = Math.round(to * (1 - Math.pow(1 - p, 3)));
        if(p < 1) requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
      cio.unobserve(el);
    });
  }, { threshold:.6 });
  document.querySelectorAll('[data-count]').forEach(function(el){ cio.observe(el); });

  /* ---------- marquees: duplicate content for seamless loop ---------- */
  document.querySelectorAll('[data-marquee]').forEach(function(tr){
    tr.innerHTML = tr.innerHTML + tr.innerHTML;
  });

  /* ---------- services: hover / focus highlight ---------- */
  document.querySelectorAll('.svc-row').forEach(function(row){
    var btn = row.querySelector('.svc-btn');
    ['mouseenter','focusin'].forEach(function(ev){ btn.addEventListener(ev, function(){ row.classList.add('is-hot'); }); });
    ['mouseleave','focusout'].forEach(function(ev){ btn.addEventListener(ev, function(){ row.classList.remove('is-hot'); }); });
  });

  /* ---------- process: active step + rail ----------
     Driven by scroll position, not an IntersectionObserver band. A narrow
     band can be jumped over between frames on fast or momentum scrolling,
     which left the middle steps (Design, Build) unhighlighted. Measuring
     which step centre sits nearest the reading line always resolves to
     exactly one, at every frame, in both directions. */
  var steps = Array.prototype.slice.call(document.querySelectorAll('.proc-step'));
  var headWords = Array.prototype.slice.call(document.querySelectorAll('#procHead span'));
  var fill = document.getElementById('procFill');
  var procActive = -1;

  function setStep(i){
    if(i === procActive) return;
    procActive = i;
    steps.forEach(function(s,n){ s.classList.toggle('is-on', n === i); });
    headWords.forEach(function(w,n){ w.classList.toggle('off', n !== i); });
    if(fill) fill.style.width = ((i+1)/steps.length*100) + '%';
  }

  function syncProc(){
    if(!steps.length) return;
    var line = window.innerHeight * 0.45;   /* the reading line */
    var best = 0, bestDist = Infinity;
    for(var i = 0; i < steps.length; i++){
      var r = steps[i].getBoundingClientRect();
      var dist = Math.abs(r.top + r.height / 2 - line);
      if(dist < bestDist){ bestDist = dist; best = i; }
    }
    setStep(best);
  }

  if(steps.length){
    var procTick = false;
    function onProcScroll(){
      if(procTick) return;
      procTick = true;
      requestAnimationFrame(function(){ syncProc(); procTick = false; });
    }
    window.addEventListener('scroll', onProcScroll, { passive:true });
    window.addEventListener('resize', onProcScroll);
    syncProc();
  }

  if(reduce) return; /* everything below is pure motion polish */

  /* ---------- magnetic buttons ---------- */
  document.querySelectorAll('.magnetic').forEach(function(btn){
    var inner = btn.querySelector('.btn-in');
    btn.addEventListener('mousemove', function(e){
      var r = btn.getBoundingClientRect();
      var x = (e.clientX - r.left - r.width/2) * .28;
      var y = (e.clientY - r.top - r.height/2) * .38;
      btn.style.transform = 'translate(' + x + 'px,' + y + 'px)';
      if(inner) inner.style.transform = 'translate(' + x*.3 + 'px,' + y*.3 + 'px)';
    });
    btn.addEventListener('mouseleave', function(){
      btn.style.transform = '';
      if(inner) inner.style.transform = '';
    });
  });

  /* ---------- hero parallax on pointer ---------- */
  var hv = document.getElementById('heroVisual');
  var rtPar = document.getElementById('rtPar');
  if(hv && window.matchMedia('(pointer:fine)').matches){
    window.addEventListener('mousemove', function(e){
      var x = (e.clientX / window.innerWidth - .5);
      var y = (e.clientY / window.innerHeight - .5);
      hv.style.transform = 'translate3d(' + (x*-14) + 'px,' + (y*-12) + 'px,0)';
      if(rtPar) rtPar.style.transform = 'translate(' + (x*10) + 'px,' + (y*8) + 'px)';
    }, { passive:true });
    hv.style.transition = 'transform .9s cubic-bezier(.16,1,.3,1)';
    if(rtPar) rtPar.style.transition = 'transform 1.2s cubic-bezier(.16,1,.3,1)';
  }

  /* ---------- work media parallax on scroll ---------- */
  var pars = Array.prototype.slice.call(document.querySelectorAll('.proj-media'));
  var ticking = false;
  function parallax(){
    var vh = window.innerHeight;
    pars.forEach(function(m){
      var r = m.getBoundingClientRect();
      if(r.bottom < -200 || r.top > vh + 200) return;
      var p = (r.top + r.height/2 - vh/2) / vh;
      var g = m.querySelector('.mpar');
      if(g) g.style.transform = 'translateY(' + (p * -26) + 'px) scale(1.03)';
    });
    ticking = false;
  }
  window.addEventListener('scroll', function(){
    if(!ticking){ ticking = true; requestAnimationFrame(parallax); }
  }, { passive:true });
  parallax();

  /* ---------- cursor ring ---------- */
  if(window.matchMedia('(pointer:fine)').matches){
    var cur = document.getElementById('cursor');
    var cx = 0, cy = 0, tx = 0, ty = 0, raf;
    window.addEventListener('mousemove', function(e){
      tx = e.clientX; ty = e.clientY;
      cur.classList.add('on');
      if(!raf) raf = requestAnimationFrame(loop);
    }, { passive:true });
    function loop(){
      cx += (tx - cx) * .18; cy += (ty - cy) * .18;
      cur.style.transform = 'translate(' + cx + 'px,' + cy + 'px)';
      raf = requestAnimationFrame(loop);
    }
    document.addEventListener('mouseover', function(e){
      var hit = e.target.closest('a,button,.svc-btn,.tag');
      cur.classList.toggle('grow', !!hit);
    });
    document.addEventListener('mouseleave', function(){ cur.classList.remove('on'); });
  }
})();

/* ============================================================
   PAGE-LEVEL BEHAVIOUR
   Shared by every page: nav indicator for the current route,
   scroll progress, sticky sub-navigation, back-to-top and the
   contact form. Runs independently of the home-page module
   above so a failure in one cannot take out the other.
   ============================================================ */
(function(){
  "use strict";
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var page = document.body.getAttribute('data-page') || '';

  /* ---------- nav indicator for the active route ---------- */
  var ind = document.getElementById('navInd');
  var current = document.querySelector('.nav-link[aria-current="page"]');
  function placeInd(){
    if(!ind || !current) return;
    ind.style.width = current.offsetWidth + 'px';
    ind.style.transform = 'translateX(' + current.offsetLeft + 'px)';
    ind.classList.add('on');
  }
  if(current){
    placeInd();
    window.addEventListener('resize', placeInd);
    if(document.fonts && document.fonts.ready) document.fonts.ready.then(placeInd);
  }

  /* ---------- scroll progress ---------- */
  var bar = document.getElementById('progress');
  if(bar){
    var barTick = false;
    function drawBar(){
      var h = document.documentElement.scrollHeight - window.innerHeight;
      var p = h > 0 ? Math.min(window.scrollY / h, 1) : 0;
      bar.style.width = (p * 100) + '%';
      barTick = false;
    }
    window.addEventListener('scroll', function(){
      if(!barTick){ barTick = true; requestAnimationFrame(drawBar); }
    }, { passive:true });
    window.addEventListener('resize', drawBar);
    drawBar();
  }

  /* ---------- sticky sub-navigation ----------
     Same reading-line approach as the process section: pick the
     section nearest the line rather than waiting for an observer
     band, so fast scrolls can never leave every chip unlit. */
  var subLinks = Array.prototype.slice.call(document.querySelectorAll('.subnav a[href^="#"]'));
  if(subLinks.length){
    var targets = subLinks.map(function(a){
      return { link:a, el:document.getElementById(a.getAttribute('href').slice(1)) };
    }).filter(function(t){ return t.el; });

    var subActive = -1, subTick = false;
    function syncSub(){
      var line = window.innerHeight * 0.32, best = 0, bestDist = Infinity;
      for(var i = 0; i < targets.length; i++){
        var r = targets[i].el.getBoundingClientRect();
        var dist = Math.abs(r.top - line);
        if(dist < bestDist){ bestDist = dist; best = i; }
      }
      if(best !== subActive){
        subActive = best;
        targets.forEach(function(t,n){ t.link.classList.toggle('is-on', n === best); });
        var chip = targets[best].link, rail = chip.parentNode;
        if(rail.scrollWidth > rail.clientWidth){
          rail.scrollTo({ left: chip.offsetLeft - rail.clientWidth / 2 + chip.offsetWidth / 2,
                          behavior: reduce ? 'auto' : 'smooth' });
        }
      }
      subTick = false;
    }
    window.addEventListener('scroll', function(){
      if(!subTick){ subTick = true; requestAnimationFrame(syncSub); }
    }, { passive:true });
    window.addEventListener('resize', syncSub);
    syncSub();
  }

  /* ---------- back to top ---------- */
  var top = document.getElementById('toTop');
  if(top){
    var topTick = false;
    function syncTop(){
      top.classList.toggle('on', window.scrollY > window.innerHeight * 1.2);
      topTick = false;
    }
    window.addEventListener('scroll', function(){
      if(!topTick){ topTick = true; requestAnimationFrame(syncTop); }
    }, { passive:true });
    top.addEventListener('click', function(){
      window.scrollTo({ top:0, behavior: reduce ? 'auto' : 'smooth' });
    });
    syncTop();
  }

  /* ---------- contact form ----------
     Front-end validation only. There is no backend: wire the form
     to your own endpoint, Formspree, or a Netlify form before launch.
     See README -> "Wiring the contact form". */
  var form = document.getElementById('projectForm');
  if(form){
    var okBox = document.getElementById('formOk');

    function fieldOf(input){ return input.closest('.field'); }
    function setBad(input, message){
      var f = fieldOf(input); if(!f) return;
      f.classList.add('is-bad');
      var e = f.querySelector('.err');
      if(e) e.textContent = message;
      input.setAttribute('aria-invalid','true');
    }
    function clearBad(input){
      var f = fieldOf(input); if(!f) return;
      f.classList.remove('is-bad');
      input.removeAttribute('aria-invalid');
    }
    function validate(input){
      var v = (input.value || '').trim();
      if(input.hasAttribute('required') && !v){
        setBad(input, 'This field is required.'); return false;
      }
      if(input.type === 'email' && v && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)){
        setBad(input, 'Enter a valid email address.'); return false;
      }
      if(input.name === 'message' && v && v.length < 20){
        setBad(input, 'A little more detail helps us reply usefully.'); return false;
      }
      clearBad(input); return true;
    }

    Array.prototype.forEach.call(form.querySelectorAll('input,textarea,select'), function(input){
      input.addEventListener('blur', function(){ if(input.value.trim()) validate(input); });
      input.addEventListener('input', function(){
        if(fieldOf(input) && fieldOf(input).classList.contains('is-bad')) validate(input);
      });
    });

    form.addEventListener('submit', function(e){
      e.preventDefault();
      var fields = Array.prototype.slice.call(form.querySelectorAll('input[required],textarea[required],select[required]'));
      var bad = fields.filter(function(f){ return !validate(f); });
      if(bad.length){
        bad[0].focus();
        bad[0].scrollIntoView({ block:'center', behavior: reduce ? 'auto' : 'smooth' });
        return;
      }
      form.hidden = true;
      if(okBox){
        okBox.classList.add('on');
        okBox.setAttribute('tabindex','-1');
        okBox.focus();
        okBox.scrollIntoView({ block:'center', behavior: reduce ? 'auto' : 'smooth' });
      }
    });
  }

  /* ---------- deep links land below the fixed header ---------- */
  if(location.hash){
    var target = document.getElementById(location.hash.slice(1));
    if(target) setTimeout(function(){
      window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - 96, behavior:'auto' });
    }, 40);
  }

  /* ---------- header adopts the surface beneath it ----------
     The header is fixed and the page alternates dark and light sections, so a
     single dark translucent bar turns muddy and low-contrast over paper. We
     measure the light sections once and flip a class as they pass under. */
  var navEl = document.getElementById('nav');
  var subEl = document.querySelector('.subnav');
  var lightEls = Array.prototype.slice.call(document.querySelectorAll('.panel-paper'));

  if(navEl && lightEls.length){
    var zones = [];
    function measureZones(){
      zones = lightEls.map(function(el){
        var r = el.getBoundingClientRect();
        return { top:r.top + window.scrollY, bottom:r.bottom + window.scrollY };
      });
    }
    function inLight(y){
      for(var i = 0; i < zones.length; i++){
        if(y > zones[i].top && y < zones[i].bottom) return true;
      }
      return false;
    }
    var themeTick = false;
    function syncTheme(){
      var navH = navEl.offsetHeight;
      navEl.classList.toggle('on-light', inLight(window.scrollY + navH * 0.55));
      if(subEl){
        subEl.classList.toggle('on-light',
          inLight(window.scrollY + navH + subEl.offsetHeight * 0.5));
      }
      themeTick = false;
    }
    window.addEventListener('scroll', function(){
      if(!themeTick){ themeTick = true; requestAnimationFrame(syncTheme); }
    }, { passive:true });
    window.addEventListener('resize', function(){ measureZones(); syncTheme(); });
    if(document.fonts && document.fonts.ready){
      document.fonts.ready.then(function(){ measureZones(); syncTheme(); });
    }
    window.addEventListener('load', function(){ measureZones(); syncTheme(); });
    measureZones();
    syncTheme();
  }

  document.documentElement.setAttribute('data-route', page);
})();
