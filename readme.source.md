
```aura width=850 height=260
<div style={{
  width: '100%', height: '100%', background: '#05070f',
  display: 'flex', alignItems: 'center', fontFamily: 'Courier New, monospace',
  position: 'relative', overflow: 'hidden', borderRadius: 16,
  border: '1px solid #00f0ff'
}}>
  <style>{`
    @keyframes scan {
      0% { top: -10px; }
      100% { top: 270px; }
    }
    @keyframes blink {
      0%, 100% { opacity: 1; }
      50% { opacity: 0; }
    }
    #scanner {
      position: absolute; left: 0; width: 100%; height: 2px;
      background: linear-gradient(90deg, transparent, #00f0ff, transparent);
      animation: scan 4s linear infinite;
      opacity: 0.3;
    }
    #cursor { animation: blink 1s step-end infinite; }
  `}</style>
  
  <div id="scanner" />

  <div style={{ display: 'flex', width: '100%', padding: '24px 32px', justifyContent: 'space-between', alignItems: 'center', zIndex: 10 }}>
    <div style={{ display: 'flex', flexDirection: 'column', gap: 4, width: '65%' }}>
      <div style={{ display: 'flex', gap: 8, fontSize: 13, color: '#6366f1' }}>
        <span>[system_init] SUCCESS</span>
        <span>|</span>
        <span>[status] READY</span>
      </div>
      
      <span style={{ fontSize: 24, fontWeight: 900, color: '#ffffff', marginTop: 10 }}>
        &gt; oldregime --identity
      </span>
      
      <div style={{ display: 'flex', flexDirection: 'column', gap: 6, marginTop: 12, fontSize: 13, color: '#00f0ff', lineHeight: 1.5 }}>
        <div style={{ display: 'flex' }}><span style={{ color: '#a5b4fc', width: 100 }}>NAME:</span><span style={{ color: '#fff' }}>Divyansh Joshi</span></div>
        <div style={{ display: 'flex' }}><span style={{ color: '#a5b4fc', width: 100 }}>ROLE:</span><span style={{ color: '#fff' }}>Systems Tinkerer & AI Architect</span></div>
        <div style={{ display: 'flex' }}><span style={{ color: '#a5b4fc', width: 100 }}>CAMPUS:</span><span style={{ color: '#fff' }}>Vellore Institute of Technology '26</span></div>
        <div style={{ display: 'flex' }}><span style={{ color: '#a5b4fc', width: 100 }}>HOMELAB:</span><span style={{ color: '#fff' }}>Proxmox cluster • TrueNAS Core • ZFS RAID</span></div>
      </div>
      
      <div style={{ display: 'flex', alignItems: 'center', gap: 4, fontSize: 13, color: '#10b981', marginTop: 12 }}>
        <span>&gt; pinging main_server... packet received.</span>
        <span id="cursor" style={{ fontWeight: 900 }}>█</span>
      </div>
    </div>

    <div style={{ display: 'flex', position: 'relative', width: 140, height: 140, alignItems: 'center', justifyContent: 'center' }}>
      <div style={{
        position: 'absolute', width: 130, height: 130, borderRadius: 65,
        border: '2px dashed #00f0ff', opacity: 0.6
      }} />
      <div style={{
        position: 'absolute', width: 120, height: 120, borderRadius: 60,
        border: '1px solid #6366f1', opacity: 0.4
      }} />
      <img
        src={github?.user?.avatarUrl ?? 'https://github.com/oldregime.png'}
        width={106} height={106}
        style={{ borderRadius: 53, border: '2px solid #00f0ff' }}
      />
    </div>
  </div>
</div>
```

<br/>

## ⚡ About Me

I'm a **B.Tech Computer Science student at Vellore Institute of Technology (VIT)** specializing in architecting highly available systems, engineering AI-driven platforms, and building secure networks. 

Whether it's deploying **LangGraph LLM workflows**, setting up **TrueNAS on Proxmox** with ZFS RAID, or writing secure **ESP32** gateways using C++, I thrive on solving complex, low-level problems with scalable code. I love transforming unstructured data into actionable insights and automating infrastructure to achieve zero-trust networking.

<br/>

```aura width=850 height=280
<div style={{
  width: '100%', height: '100%', background: '#05070f',
  display: 'flex', flexDirection: 'column', padding: '24px',
  fontFamily: 'Courier New, monospace', borderRadius: 16,
  border: '1px solid #6366f1'
}}>
  <span style={{ fontSize: 15, fontWeight: 900, color: '#00f0ff', marginBottom: 16, letterSpacing: '1px' }}>
    &gt; sysctl --list tech_specs
  </span>

  <div style={{ display: 'flex', flexDirection: 'column', gap: 16, flex: 1 }}>
    <div style={{ display: 'flex', gap: 16, flex: 1 }}>
      <div style={{
        display: 'flex', flexDirection: 'column', flex: 1, padding: 14,
        background: 'rgba(0,240,255,0.01)', border: '1px solid rgba(0,240,255,0.1)', borderRadius: 8
      }}>
        <span style={{ fontSize: 12, fontWeight: 900, color: '#00f0ff', marginBottom: 8 }}>[01] EXECUTION_ENGINES</span>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
          {['Python', 'C++', 'TypeScript', 'JavaScript', 'Java'].map(function(t) {
            return (
              <div key={t} style={{
                fontSize: 11, fontWeight: 700, color: '#fff', padding: '4px 8px',
                background: 'rgba(0, 240, 255, 0.05)', border: '1px solid rgba(0, 240, 255, 0.2)', borderRadius: 4
              }}>{t}</div>
            );
          })}
        </div>
      </div>

      <div style={{
        display: 'flex', flexDirection: 'column', flex: 1, padding: 14,
        background: 'rgba(99,102,241,0.01)', border: '1px solid rgba(99,102,241,0.1)', borderRadius: 8
      }}>
        <span style={{ fontSize: 12, fontWeight: 900, color: '#a5b4fc', marginBottom: 8 }}>[02] NEURAL_CORE_AI</span>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
          {['LangGraph', 'Genkit Flow', 'Llama-3.1', 'Streamlit', 'Pandas'].map(function(t) {
            return (
              <div key={t} style={{
                fontSize: 11, fontWeight: 700, color: '#fff', padding: '4px 8px',
                background: 'rgba(99, 102, 241, 0.05)', border: '1px solid rgba(99, 102, 241, 0.2)', borderRadius: 4
              }}>{t}</div>
            );
          })}
        </div>
      </div>
    </div>

    <div style={{ display: 'flex', gap: 16, flex: 1 }}>
      <div style={{
        display: 'flex', flexDirection: 'column', flex: 1, padding: 14,
        background: 'rgba(16,185,129,0.01)', border: '1px solid rgba(16,185,129,0.1)', borderRadius: 8
      }}>
        <span style={{ fontSize: 12, fontWeight: 900, color: '#10b981', marginBottom: 8 }}>[03] WEB_ORCHESTRATION</span>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
          {['Next.js', 'React', 'Tailwind', 'Node.js', 'REST APIs'].map(function(t) {
            return (
              <div key={t} style={{
                fontSize: 11, fontWeight: 700, color: '#fff', padding: '4px 8px',
                background: 'rgba(16, 185, 129, 0.05)', border: '1px solid rgba(16, 185, 129, 0.2)', borderRadius: 4
              }}>{t}</div>
            );
          })}
        </div>
      </div>

      <div style={{
        display: 'flex', flexDirection: 'column', flex: 1, padding: 14,
        background: 'rgba(245,158,11,0.01)', border: '1px solid rgba(245,158,11,0.1)', borderRadius: 8
      }}>
        <span style={{ fontSize: 12, fontWeight: 900, color: '#f59e0b', marginBottom: 8 }}>[04] METAL_STACK_DB</span>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
          {['Proxmox', 'TrueNAS', 'ZFS RAID', 'Docker', 'PostgreSQL', 'Supabase'].map(function(t) {
            return (
              <div key={t} style={{
                fontSize: 11, fontWeight: 700, color: '#fff', padding: '4px 8px',
                background: 'rgba(245, 158, 11, 0.05)', border: '1px solid rgba(245, 158, 11, 0.2)', borderRadius: 4
              }}>{t}</div>
            );
          })}
        </div>
      </div>
    </div>
  </div>
</div>
```

<br/>

```aura width=850 height=380
<div style={{
  width: '100%', height: '100%', background: '#05070f',
  display: 'flex', flexDirection: 'column', padding: '24px',
  fontFamily: 'Courier New, monospace', borderRadius: 16,
  border: '1px solid #10b981'
}}>
  <span style={{ fontSize: 15, fontWeight: 900, color: '#10b981', marginBottom: 16, letterSpacing: '1px' }}>
    {'> docker ps --format "table {{.Names}}\\t{{.Status}}\\t{{.Ports}}"'}
  </span>

  <div style={{ display: 'flex', flexDirection: 'column', gap: 14, flex: 1 }}>
    <div style={{ display: 'flex', gap: 14, flex: 1 }}>
      <div style={{
        display: 'flex', flexDirection: 'column', flex: 1, padding: 14,
        background: 'rgba(0,240,255,0.01)', border: '1px solid rgba(16,185,129,0.15)', borderRadius: 8,
        justifyContent: 'space-between'
      }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ fontSize: 13, fontWeight: 900, color: '#fff' }}>SG_WOL_GATEWAY</span>
            <span style={{ fontSize: 10, fontWeight: 900, color: '#10b981', letterSpacing: '0.5px' }}>● ONLINE</span>
          </div>
          <span style={{ fontSize: 11, color: '#94a3b8', lineHeight: 1.4 }}>
            Secure ESP32 Wake-on-LAN gateway. TrueNAS REST APIs over Telegram Bot without exposing ports.
          </span>
        </div>
        <div style={{ display: 'flex', gap: 4, marginTop: 8 }}>
          {['ESP32', 'C++', 'Python', 'Telegram'].map(function(t) {
            return (
              <span key={t} style={{ fontSize: 9, fontWeight: 700, color: '#38bdf8', background: 'rgba(56,189,248,0.05)', border: '1px solid rgba(56,189,248,0.15)', padding: '2px 6px', borderRadius: 4 }}>{t}</span>
            );
          })}
        </div>
      </div>

      <div style={{
        display: 'flex', flexDirection: 'column', flex: 1, padding: 14,
        background: 'rgba(0,240,255,0.01)', border: '1px solid rgba(16,185,129,0.15)', borderRadius: 8,
        justifyContent: 'space-between'
      }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ fontSize: 13, fontWeight: 900, color: '#fff' }}>CLINICAL_MATCH</span>
            <span style={{ fontSize: 10, fontWeight: 900, color: '#38bdf8', letterSpacing: '0.5px' }}>● ACTIVE_AGENT</span>
          </div>
          <span style={{ fontSize: 11, color: '#94a3b8', lineHeight: 1.4 }}>
            LangGraph AI pipeline mapping clinical trials. Parses PyPDF to analyze patient eligibility in under 5 seconds.
          </span>
        </div>
        <div style={{ display: 'flex', gap: 4, marginTop: 8 }}>
          {['LangGraph', 'Groq', 'Streamlit', 'PyPDF'].map(function(t) {
            return (
              <span key={t} style={{ fontSize: 9, fontWeight: 700, color: '#a5b4fc', background: 'rgba(165,180,252,0.05)', border: '1px solid rgba(165,180,252,0.15)', padding: '2px 6px', borderRadius: 4 }}>{t}</span>
            );
          })}
        </div>
      </div>
    </div>

    <div style={{ display: 'flex', gap: 14, flex: 1 }}>
      <div style={{
        display: 'flex', flexDirection: 'column', flex: 1, padding: 14,
        background: 'rgba(0,240,255,0.01)', border: '1px solid rgba(16,185,129,0.15)', borderRadius: 8,
        justifyContent: 'space-between'
      }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ fontSize: 13, fontWeight: 900, color: '#fff' }}>PROX_NAS_CLUSTER</span>
            <span style={{ fontSize: 10, fontWeight: 900, color: '#fb7185', letterSpacing: '0.5px' }}>● 99.9%_UPTIME</span>
          </div>
          <span style={{ fontSize: 11, color: '#94a3b8', lineHeight: 1.4 }}>
            High-availability homelab NAS. REST APIs for automated Python provisioning, ZFS RAID, and Tailscale mesh.
          </span>
        </div>
        <div style={{ display: 'flex', gap: 4, marginTop: 8 }}>
          {['Proxmox', 'TrueNAS', 'ZFS', 'Python'].map(function(t) {
            return (
              <span key={t} style={{ fontSize: 9, fontWeight: 700, color: '#fb7185', background: 'rgba(251,113,133,0.05)', border: '1px solid rgba(251,113,133,0.15)', padding: '2px 6px', borderRadius: 4 }}>{t}</span>
            );
          })}
        </div>
      </div>

      <div style={{
        display: 'flex', flexDirection: 'column', flex: 1, padding: 14,
        background: 'rgba(0,240,255,0.01)', border: '1px solid rgba(16,185,129,0.15)', borderRadius: 8,
        justifyContent: 'space-between'
      }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ fontSize: 13, fontWeight: 900, color: '#fff' }}>GRADEWISE_FLOW</span>
            <span style={{ fontSize: 10, fontWeight: 900, color: '#cbd5e1', letterSpacing: '0.5px' }}>● DEPLOYED</span>
          </div>
          <span style={{ fontSize: 11, color: '#94a3b8', lineHeight: 1.4 }}>
            Full-stack student paper grading tool. Automates feedback generation utilizing Genkit on Google Cloud.
          </span>
        </div>
        <div style={{ display: 'flex', gap: 4, marginTop: 8 }}>
          {['Next.js', 'React', 'GenkitFlow', 'GCP'].map(function(t) {
            return (
              <span key={t} style={{ fontSize: 9, fontWeight: 700, color: '#cbd5e1', background: 'rgba(203,213,225,0.05)', border: '1px solid rgba(203,213,225,0.15)', padding: '2px 6px', borderRadius: 4 }}>{t}</span>
            );
          })}
        </div>
      </div>
    </div>
  </div>
</div>
```

<br/>

```aura width=850 height=220
<div style={{
  width: '100%', height: '100%', background: '#05070f',
  display: 'flex', padding: '24px', fontFamily: 'Courier New, monospace', borderRadius: 16,
  border: '1px solid #00f0ff', alignItems: 'center'
}}>
  <div style={{ display: 'flex', flexDirection: 'column', width: '45%', paddingRight: 24, borderRight: '1px solid rgba(0,240,255,0.15)' }}>
    <span style={{ fontSize: 13, fontWeight: 900, color: '#00f0ff', letterSpacing: '0.5px', marginBottom: 16 }}>
      &gt; monitor --telemetry
    </span>
    <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
      <div style={{ display: 'flex', gap: 10 }}>
        <div style={{ display: 'flex', flexDirection: 'column', flex: 1, padding: '10px 14px', background: 'rgba(0,240,255,0.01)', border: '1px solid rgba(0,240,255,0.08)', borderRadius: 6 }}>
          <span style={{ fontSize: 10, fontWeight: 900, color: '#94a3b8' }}>COMPILATIONS</span>
          <span style={{ fontSize: 18, fontWeight: 900, color: '#fff', marginTop: 2 }}>{github?.stats?.totalCommits ?? 1547}</span>
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', flex: 1, padding: '10px 14px', background: 'rgba(0,240,255,0.01)', border: '1px solid rgba(0,240,255,0.08)', borderRadius: 6 }}>
          <span style={{ fontSize: 10, fontWeight: 900, color: '#94a3b8' }}>UPVOTES</span>
          <span style={{ fontSize: 18, fontWeight: 900, color: '#fbbf24', marginTop: 2 }}>{github?.stats?.totalStars ?? 128}</span>
        </div>
      </div>
      <div style={{ display: 'flex', gap: 10 }}>
        <div style={{ display: 'flex', flexDirection: 'column', flex: 1, padding: '10px 14px', background: 'rgba(0,240,255,0.01)', border: '1px solid rgba(0,240,255,0.08)', borderRadius: 6 }}>
          <span style={{ fontSize: 10, fontWeight: 900, color: '#94a3b8' }}>FORKS_SPAWNED</span>
          <span style={{ fontSize: 18, fontWeight: 900, color: '#38bdf8', marginTop: 2 }}>{github?.stats?.totalForks ?? 34}</span>
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', flex: 1, padding: '10px 14px', background: 'rgba(0,240,255,0.01)', border: '1px solid rgba(0,240,255,0.08)', borderRadius: 6 }}>
          <span style={{ fontSize: 10, fontWeight: 900, color: '#94a3b8' }}>TARGET_REPOS</span>
          <span style={{ fontSize: 18, fontWeight: 900, color: '#34d399', marginTop: 2 }}>{github?.stats?.totalRepos ?? 25}</span>
        </div>
      </div>
    </div>
  </div>

  <div style={{ display: 'flex', flexDirection: 'column', width: '55%', paddingLeft: 24 }}>
    <span style={{ fontSize: 13, fontWeight: 900, color: '#00f0ff', letterSpacing: '0.5px', marginBottom: 12 }}>
      &gt; cat /var/log/languages
    </span>
    
    <div style={{ display: 'flex', width: '100%', height: 12, borderRadius: 3, overflow: 'hidden', backgroundColor: 'rgba(255,255,255,0.05)', marginBottom: 16 }}>
      {((github && github.languages && github.languages.length > 0) ? github.languages.slice(0, 5) : [
        { name: 'TypeScript', percentage: 45, color: '#3178c6' },
        { name: 'JavaScript', percentage: 25, color: '#f1e05a' },
        { name: 'Python', percentage: 15, color: '#3572A5' },
        { name: 'C++', percentage: 10, color: '#f34b7d' },
        { name: 'Other', percentage: 5, color: '#858585' }
      ]).map(function(l) {
        return (
          <div key={l.name} style={{ width: `${l.percentage}%`, height: '100%', backgroundColor: l.color ?? '#858585' }} />
        );
      })}
    </div>

    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px 16px' }}>
      {((github && github.languages && github.languages.length > 0) ? github.languages.slice(0, 5) : [
        { name: 'TypeScript', percentage: 45, color: '#3178c6' },
        { name: 'JavaScript', percentage: 25, color: '#f1e05a' },
        { name: 'Python', percentage: 15, color: '#3572A5' },
        { name: 'C++', percentage: 10, color: '#f34b7d' },
        { name: 'Other', percentage: 5, color: '#858585' }
      ]).map(function(l) {
        return (
          <div key={l.name} style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <div style={{ width: 8, height: 8, borderRadius: 4, backgroundColor: l.color ?? '#858585' }} />
            <span style={{ fontSize: 11, fontWeight: 700, color: '#cbd5e1' }}>{l.name}</span>
            <span style={{ fontSize: 11, color: '#94a3b8' }}>{l.percentage}%</span>
          </div>
        );
      })}
    </div>
  </div>
</div>
```

<br/>

<div align="center">
  <i>"Simplicity is the ultimate sophistication."</i><br><br>
  <a href="https://linkedin.com/in/divyanshjoshidev">Let's connect and build something awesome together! 🚀</a>
</div>
