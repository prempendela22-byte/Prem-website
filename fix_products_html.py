with open("products.html", "r", encoding="utf-8") as f:
    text = f.read()

prefix = text.split('    <!-- Engine Parts -->')[0]
suffix = text.split('  <footer>\\n    <p><strong>🏍️ Sankar Motors</strong></p>')[1] if '  <footer>\\n    <p><strong>🏍️ Sankar Motors</strong></p>' in text else text.split('  <footer>')[1]

html_body = """    <!-- Engine Parts -->
    <div class="category-section">
      <h3 class="category-title"><i class="fa-solid fa-gear"></i> Engine Parts</h3>
      <div class="products-grid">
        <div class="product-card">
          <div class="product-icon"><svg viewBox="0 0 64 64" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><rect x="12" y="16" width="40" height="32" rx="4" /><path d="M12 24h40M12 32h40M12 40h40" /><path d="M24 16v32M32 16v32M40 16v32" opacity="0.4" /></svg></div>
          <div class="product-info">
            <div class="product-badge">Popular</div>
            <div class="product-name">Air Filter</div>
            <div class="product-desc">Clean engine air inlet. Improves fuel efficiency and engine performance.</div>
            <a href="order.html" class="cta-btn">Order Now</a>
          </div>
        </div>

        <div class="product-card">
          <div class="product-icon"><svg viewBox="0 0 64 64" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M16 20c0-6 7.2-10 16-10s16 4 16 10v24c0 6-7.2 10-16 10s-16-4-16-10V20z"/><path d="M16 20c0 6 7.2 10 16 10s16-4 16-10" /><circle cx="32" cy="18" r="3" fill="currentColor"/><circle cx="24" cy="18" r="2" fill="currentColor"/><circle cx="40" cy="18" r="2" fill="currentColor"/></svg></div>
          <div class="product-info">
            <div class="product-badge">Essential</div>
            <div class="product-name">Oil Filter</div>
            <div class="product-desc">Keeps engine oil clean. Replace every service for optimal engine health.</div>
            <a href="order.html" class="cta-btn">Order Now</a>
          </div>
        </div>

        <div class="product-card">
          <div class="product-icon"><svg viewBox="0 0 64 64" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M32 2v6" /><path d="M26 8h12v12H26z" fill="currentColor" fill-opacity="0.2"/><path d="M22 20h20v6H22z" /><path d="M26 26h12v14H26z" /><path d="M26 30h12M26 34h12M26 38h12" /><path d="M32 40v14c0 4-6 4-6 4" /></svg></div>
          <div class="product-info">
            <div class="product-name">Spark Plug</div>
            <div class="product-desc">Essential for ignition. Improves mileage and engine performance.</div>
            <a href="order.html" class="cta-btn">Order Now</a>
          </div>
        </div>

        <div class="product-card">
          <div class="product-icon"><svg viewBox="0 0 64 64" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M32 8c-13.3 0-24 10.7-24 24s10.7 24 24 24 24-10.7 24-24S45.3 8 32 8z" stroke-dasharray="6 4" /><circle cx="32" cy="32" r="14" /><circle cx="32" cy="16" r="3" fill="currentColor"/><circle cx="32" cy="48" r="3" fill="currentColor"/><circle cx="16" cy="32" r="3" fill="currentColor"/><circle cx="48" cy="32" r="3" fill="currentColor"/></svg></div>
          <div class="product-info">
            <div class="product-name">Engine Gasket</div>
            <div class="product-desc">Prevents oil leaks. Maintains engine seal integrity.</div>
            <a href="order.html" class="cta-btn">Order Now</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Brake & Suspension -->
    <div class="category-section">
      <h3 class="category-title"><i class="fa-solid fa-stop"></i> Brake &amp; Suspension</h3>
      <div class="products-grid">
        <div class="product-card">
          <div class="product-icon"><svg viewBox="0 0 64 64" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 24c0-8 12-16 20-16s20 8 20 16v16c0 4-4 8-8 8H20c-4 0-8-4-8-8V24z" fill="currentColor" fill-opacity="0.2"/><path d="M18 24c0-4.4 7-8 14-8s14 3.6 14 8v12c0 2.2-2 4-4 4H22c-2 0-4-1.8-4-4V24z" /><circle cx="20" cy="16" r="2" fill="currentColor"/><circle cx="44" cy="16" r="2" fill="currentColor"/></svg></div>
          <div class="product-info">
            <div class="product-badge">Safety</div>
            <div class="product-name">Brake Pad</div>
            <div class="product-desc">Premium quality brake pads. Ensure safe stopping and ride comfort.</div>
            <a href="order.html" class="cta-btn">Order Now</a>
          </div>
        </div>

        <div class="product-card">
          <div class="product-icon"><svg viewBox="0 0 64 64" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M26 8h12v6H26z" /><path d="M28 14v6l-6 6v26c0 2 2 4 4 4h12c2 0 4-2 4-4V26l-6-6v-6" /><path d="M22 36h20" /><path d="M32 40c-2 0-4 2-4 4 0 2.2 1.8 4 4 4s4-1.8 4-4c0-2-2-4-4-4z" fill="currentColor"/></svg></div>
          <div class="product-info">
            <div class="product-badge">Safety</div>
            <div class="product-name">Brake Fluid</div>
            <div class="product-desc">High quality brake fluid. Maintains consistent braking performance.</div>
            <a href="order.html" class="cta-btn">Order Now</a>
          </div>
        </div>

        <div class="product-card">
          <div class="product-icon"><svg viewBox="0 0 64 64" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><circle cx="32" cy="8" r="4" /><path d="M32 12v40" /><path d="M24 20h16v16H24z" fill="currentColor" fill-opacity="0.2" /><path d="M22 16l20 6M22 26l20 6M22 36l20 6M22 46l20 6" /><circle cx="32" cy="56" r="4" /></svg></div>
          <div class="product-info">
            <div class="product-name">Shock Absorber</div>
            <div class="product-desc">Smooth ride quality. Absorbs road bumps and vibrations.</div>
            <a href="order.html" class="cta-btn">Order Now</a>
          </div>
        </div>

        <div class="product-card">
          <div class="product-icon"><svg viewBox="0 0 64 64" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8h32M16 56h32" /><path d="M32 8v4M32 52v4" /><path d="M24 12l16 8-16 8 16 8-16 8 16 8" /></svg></div>
          <div class="product-info">
            <div class="product-name">Spring Assembly</div>
            <div class="product-desc">Maintains suspension height. Ensures comfort and safety.</div>
            <a href="order.html" class="cta-btn">Order Now</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Electrical Parts -->
    <div class="category-section">
      <h3 class="category-title"><i class="fa-solid fa-plug"></i> Electrical Parts</h3>
      <div class="products-grid">
        <div class="product-card">
          <div class="product-icon"><svg viewBox="0 0 64 64" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><rect x="12" y="20" width="40" height="32" rx="2" /><path d="M20 20v-6h8v6M36 20v-6h8v6" /><path d="M24 10v4M22 12h4" /><path d="M38 12h4" /><path d="M12 30h40" /><path d="M24 40v4M22 42h4M38 42h4" /></svg></div>
          <div class="product-info">
            <div class="product-badge">Popular</div>
            <div class="product-name">Battery</div>
            <div class="product-desc">Long-lasting power. Reliable starting and performance.</div>
            <a href="order.html" class="cta-btn">Order Now</a>
          </div>
        </div>

        <div class="product-card">
          <div class="product-icon"><svg viewBox="0 0 64 64" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M32 6c-8.8 0-16 7.2-16 16 0 6.6 4 12.3 9.8 14.8V44h12v-7.2C43.6 34.3 48 28.6 48 22c0-8.8-7.2-16-16-16z" fill="currentColor" fill-opacity="0.1"/><path d="M26 44h12v6H26zM28 50h8v4h-8z" /><path d="M28 22l4-6 4 6" /><path d="M26 30h12" /></svg></div>
          <div class="product-info">
            <div class="product-name">Headlight Bulb</div>
            <div class="product-desc">Bright and clear visibility. Safe night riding.</div>
            <a href="order.html" class="cta-btn">Order Now</a>
          </div>
        </div>

        <div class="product-card">
          <div class="product-icon"><svg viewBox="0 0 64 64" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M48 24C48 10 32 6 32 6S16 10 16 24v16c0 10 16 18 16 18s16-8 16-18V24z" fill="currentColor" fill-opacity="0.2"/><path d="M16 26h32M18 36h28" /><circle cx="32" cy="16" r="3" fill="currentColor"/></svg></div>
          <div class="product-info">
            <div class="product-name">Tail Light</div>
            <div class="product-desc">Safety lighting. Ensures visibility from behind.</div>
            <a href="order.html" class="cta-btn">Order Now</a>
          </div>
        </div>

        <div class="product-card">
          <div class="product-icon"><svg viewBox="0 0 64 64" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M12 12h10v8H12zM42 44h10v8H42zM12 44h10v8H12zM42 12h10v8H42z" fill="currentColor" fill-opacity="0.3"/><path d="M22 16c10 0 10 32 20 32M22 48c10 0 10-32 20-32" /><path d="M32 32l10 10" /></svg></div>
          <div class="product-info">
            <div class="product-name">Wiring Harness</div>
            <div class="product-desc">Complete electrical connections. Reliable power distribution.</div>
            <a href="order.html" class="cta-btn">Order Now</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Body & Accessories -->
    <div class="category-section">
      <h3 class="category-title"><i class="fa-solid fa-screwdriver-wrench"></i> Body &amp; Accessories</h3>
      <div class="products-grid">
        <div class="product-card">
          <div class="product-icon"><svg viewBox="0 0 64 64" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><circle cx="32" cy="32" r="16" stroke-dasharray="6 4" /><circle cx="32" cy="32" r="6" /><path d="M16 32a16 16 0 0 1 16-16h24M16 32a16 16 0 0 0 16 16h24" /><circle cx="56" cy="16" r="3" fill="currentColor"/><circle cx="56" cy="48" r="3" fill="currentColor"/><path d="M56 16v32" stroke-dasharray="4 4" /></svg></div>
          <div class="product-info">
            <div class="product-name">Chain &amp; Sprocket</div>
            <div class="product-desc">Power transmission. Smooth acceleration and control.</div>
            <a href="order.html" class="cta-btn">Order Now</a>
          </div>
        </div>

        <div class="product-card">
          <div class="product-icon"><svg viewBox="0 0 64 64" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M40 10L10 40l14 14L54 24z" fill="currentColor" fill-opacity="0.1"/><path d="M20 30l14-14" /><path d="M52 8l2 6 6 2-6 2-2 6-2-6-6-2 6-2z" fill="currentColor"/><path d="M14 56l1 3 3 1-3 1-1 3-1-3-3-1 3-1z" fill="currentColor"/></svg></div>
          <div class="product-info">
            <div class="product-name">Chrome Plating</div>
            <div class="product-desc">Decorative finishes. Enhances bike appearance.</div>
            <a href="order.html" class="cta-btn">Order Now</a>
          </div>
        </div>
      </div>
    </div>

  </div>

  <footer>
"""

# write back the fixed file
with open("products.html", "w", encoding="utf-8") as f:
    f.write(prefix + html_body + suffix)

