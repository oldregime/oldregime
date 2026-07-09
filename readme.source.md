
```aura width=850 height=240
<div style={{
  width: '100%', height: '100%', background: '#09090e',
  display: 'flex', alignItems: 'center', fontFamily: 'Inter, sans-serif',
  position: 'relative', overflow: 'hidden', borderRadius: 16,
  border: '1px solid rgba(99, 102, 241, 0.2)'
}}>
  <svg width="850" height="240" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="g1" cx="20%" cy="30%" r="50%">
        <stop offset="0%" stopColor="rgba(99, 102, 241, 0.25)" />
        <stop offset="100%" stopColor="rgba(99, 102, 241, 0)" />
      </radialGradient>
      <radialGradient id="g2" cx="80%" cy="70%" r="50%">
        <stop offset="0%" stopColor="rgba(6, 182, 212, 0.2)" />
        <stop offset="100%" stopColor="rgba(6, 182, 212, 0)" />
      </radialGradient>
    </defs>
    <rect width="850" height="240" fill="none" />
    <circle cx="150" cy="80" r="220" fill="url(#g1)" />
    <circle cx="700" cy="180" r="250" fill="url(#g2)" />
  </svg>

  <div style={{ display: 'flex', width: '100%', padding: '0 40px', alignItems: 'center', justifyContent: 'space-between', zIndex: 10 }}>
    <div style={{ display: 'flex', flexDirection: 'column', gap: 6, maxWidth: 500 }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
        <span style={{ fontSize: 13, fontWeight: 700, color: '#6366f1', textTransform: 'uppercase', letterSpacing: '2px' }}>
          Portfolio Profile
        </span>
        <div style={{ width: 6, height: 6, borderRadius: 3, backgroundColor: '#06b6d4' }} />
        <span style={{ fontSize: 12, color: '#94a3b8', fontWeight: 500 }}>VIT Bhopal '26</span>
      </div>
      
      <span style={{ fontSize: 32, fontWeight: 900, color: '#ffffff', letterSpacing: '-0.5px', marginTop: 4 }}>
        Divyansh Joshi
      </span>
      
      <span style={{ fontSize: 15, fontWeight: 500, color: '#06b6d4', marginTop: 2 }}>
        Full-Stack Engineer • AI & Infrastructure Architect
      </span>
      
      <span style={{ fontSize: 13, color: '#cbd5e1', lineHeight: 1.5, marginTop: 4 }}>
        Architecting highly available systems, engineering AI-driven platforms, and building secure networks.
      </span>

      <div style={{ display: 'flex', gap: 12, marginTop: 12 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, padding: '4px 10px', borderRadius: 6, background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.06)' }}>
          <span style={{ fontSize: 11, color: '#94a3b8', fontWeight: 600 }}>📧 divyanshjoshidev@gmail.com</span>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, padding: '4px 10px', borderRadius: 6, background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.06)' }}>
          <span style={{ fontSize: 11, color: '#94a3b8', fontWeight: 600 }}>🔗 linkedin.com/in/divyanshjoshidev</span>
        </div>
      </div>
    </div>

    <div style={{ display: 'flex', position: 'relative', width: 130, height: 130, alignItems: 'center', justifyContent: 'center' }}>
      <div style={{
        position: 'absolute', width: 124, height: 124, borderRadius: 62,
        background: 'linear-gradient(135deg, #6366f1, #06b6d4)',
        opacity: 0.8
      }} />
      <div style={{
        position: 'absolute', width: 118, height: 118, borderRadius: 59,
        background: '#09090e'
      }} />
      <img
        src={github?.user?.avatarUrl ?? 'https://github.com/oldregime.png'}
        width={112} height={112}
        style={{ borderRadius: 56 }}
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
  width: '100%', height: '100%', background: '#09090e',
  display: 'flex', flexDirection: 'column', padding: '24px',
  fontFamily: 'Inter, sans-serif', borderRadius: 16,
  border: '1px solid rgba(255, 255, 255, 0.05)'
}}>
  <span style={{ fontSize: 15, fontWeight: 800, marginBottom: 16, letterSpacing: '0.5px', textTransform: 'uppercase', color: '#818cf8' }}>
    🚀 Tech Arsenal
  </span>

  <div style={{ display: 'flex', flexDirection: 'column', gap: 16, flex: 1 }}>
    <div style={{ display: 'flex', gap: 16, flex: 1 }}>
      <div style={{
        display: 'flex', flexDirection: 'column', flex: 1, padding: 14,
        background: 'rgba(255,255,255,0.01)', border: '1px solid rgba(255,255,255,0.04)', borderRadius: 10
      }}>
        <span style={{ fontSize: 12, fontWeight: 700, color: '#a5b4fc', marginBottom: 8 }}>🧠 AI & Data Engineering</span>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
          {['LangChain', 'Pandas', 'NumPy', 'Streamlit', 'Genkit'].map(t => (
            <div key={t} style={{
              fontSize: 11, fontWeight: 600, color: '#cbd5e1', padding: '4px 8px',
              background: 'rgba(99, 102, 241, 0.08)', border: '1px solid rgba(99, 102, 241, 0.15)', borderRadius: 6
            }}>{t}</div>
          ))}
        </div>
      </div>

      <div style={{
        display: 'flex', flexDirection: 'column', flex: 1, padding: 14,
        background: 'rgba(255,255,255,0.01)', border: '1px solid rgba(255,255,255,0.04)', borderRadius: 10
      }}>
        <span style={{ fontSize: 12, fontWeight: 700, color: '#38bdf8', marginBottom: 8 }}>💻 Core Languages</span>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
          {['Python', 'Java', 'C++', 'JavaScript', 'TypeScript'].map(t => (
            <div key={t} style={{
              fontSize: 11, fontWeight: 600, color: '#cbd5e1', padding: '4px 8px',
              background: 'rgba(56, 189, 248, 0.08)', border: '1px solid rgba(56, 189, 248, 0.15)', borderRadius: 6
            }}>{t}</div>
          ))}
        </div>
      </div>
    </div>

    <div style={{ display: 'flex', gap: 16, flex: 1 }}>
      <div style={{
        display: 'flex', flexDirection: 'column', flex: 1, padding: 14,
        background: 'rgba(255,255,255,0.01)', border: '1px solid rgba(255,255,255,0.04)', borderRadius: 10
      }}>
        <span style={{ fontSize: 12, fontWeight: 700, color: '#34d399', marginBottom: 8 }}>🌐 Web & Full-Stack</span>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
          {['React', 'Next.js', 'Tailwind CSS', 'Node.js', 'REST APIs'].map(t => (
            <div key={t} style={{
              fontSize: 11, fontWeight: 600, color: '#cbd5e1', padding: '4px 8px',
              background: 'rgba(52, 211, 153, 0.08)', border: '1px solid rgba(52, 211, 153, 0.15)', borderRadius: 6
            }}>{t}</div>
          ))}
        </div>
      </div>

      <div style={{
        display: 'flex', flexDirection: 'column', flex: 1, padding: 14,
        background: 'rgba(255,255,255,0.01)', border: '1px solid rgba(255,255,255,0.04)', borderRadius: 10
      }}>
        <span style={{ fontSize: 12, fontWeight: 700, color: '#fb7185', marginBottom: 8 }}>☁️ Cloud, DB & Infra</span>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
          {['AWS', 'GCP', 'Docker', 'Proxmox', 'Supabase', 'PostgreSQL', 'ZFS'].map(t => (
            <div key={t} style={{
              fontSize: 11, fontWeight: 600, color: '#cbd5e1', padding: '4px 8px',
              background: 'rgba(251, 113, 133, 0.08)', border: '1px solid rgba(251, 113, 133, 0.15)', borderRadius: 6
            }}>{t}</div>
          ))}
        </div>
      </div>
    </div>
  </div>
</div>
```

<br/>

```aura width=850 height=380
<div style={{
  width: '100%', height: '100%', background: '#09090e',
  display: 'flex', flexDirection: 'column', padding: '24px',
  fontFamily: 'Inter, sans-serif', borderRadius: 16,
  border: '1px solid rgba(255, 255, 255, 0.05)'
}}>
  <span style={{ fontSize: 15, fontWeight: 800, marginBottom: 16, letterSpacing: '0.5px', textTransform: 'uppercase', color: '#818cf8' }}>
    🚀 Featured Projects & Experience
  </span>

  <div style={{ display: 'flex', flexDirection: 'column', gap: 14, flex: 1 }}>
    <div style={{ display: 'flex', gap: 14, flex: 1 }}>
      <div style={{
        display: 'flex', flexDirection: 'column', flex: 1, padding: 14,
        background: 'rgba(255,255,255,0.01)', border: '1px solid rgba(255,255,255,0.04)', borderRadius: 10,
        justifyContent: 'space-between'
      }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ fontSize: 13, fontWeight: 700, color: '#ffffff' }}>NAS Server Dev</span>
            <span style={{ fontSize: 10, fontWeight: 600, color: '#f59e0b', background: 'rgba(245,158,11,0.08)', padding: '2px 6px', borderRadius: 4 }}>LNJ Corporate</span>
          </div>
          <span style={{ fontSize: 11, color: '#cbd5e1', lineHeight: 1.4 }}>
            Architected highly available Proxmox/TrueNAS NAS with ZFS RAID. Enabled zero-trust access for 15+ concurrent users.
          </span>
        </div>
        <div style={{ display: 'flex', gap: 4, marginTop: 8 }}>
          {['Proxmox', 'TrueNAS', 'ZFS', 'Tailscale'].map(t => (
            <span key={t} style={{ fontSize: 9, fontWeight: 600, color: '#94a3b8', background: 'rgba(255,255,255,0.04)', padding: '2px 6px', borderRadius: 4 }}>{t}</span>
          ))}
        </div>
      </div>

      <div style={{
        display: 'flex', flexDirection: 'column', flex: 1, padding: 14,
        background: 'rgba(255,255,255,0.01)', border: '1px solid rgba(255,255,255,0.04)', borderRadius: 10,
        justifyContent: 'space-between'
      }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ fontSize: 13, fontWeight: 700, color: '#ffffff' }}>Medical AI Suite</span>
            <span style={{ fontSize: 10, fontWeight: 600, color: '#10b981', background: 'rgba(16,185,129,0.08)', padding: '2px 6px', borderRadius: 4 }}>Clinical Match</span>
          </div>
          <span style={{ fontSize: 11, color: '#cbd5e1', lineHeight: 1.4 }}>
            AI platform mapping patient profiles against ClinicalTrials.gov API. Reduced manual screening time by over 90%.
          </span>
        </div>
        <div style={{ display: 'flex', gap: 4, marginTop: 8 }}>
          {['LangGraph', 'Groq', 'Streamlit', 'PyPDF'].map(t => (
            <span key={t} style={{ fontSize: 9, fontWeight: 600, color: '#94a3b8', background: 'rgba(255,255,255,0.04)', padding: '2px 6px', borderRadius: 4 }}>{t}</span>
          ))}
        </div>
      </div>
    </div>

    <div style={{ display: 'flex', gap: 14, flex: 1 }}>
      <div style={{
        display: 'flex', flexDirection: 'column', flex: 1, padding: 14,
        background: 'rgba(255,255,255,0.01)', border: '1px solid rgba(255,255,255,0.04)', borderRadius: 10,
        justifyContent: 'space-between'
      }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ fontSize: 13, fontWeight: 700, color: '#ffffff' }}>IoT Remote Access</span>
            <span style={{ fontSize: 10, fontWeight: 600, color: '#6366f1', background: 'rgba(99,102,241,0.08)', padding: '2px 6px', borderRadius: 4 }}>Hardware</span>
          </div>
          <span style={{ fontSize: 11, color: '#cbd5e1', lineHeight: 1.4 }}>
            Secure ESP32 gateway triggering Wake-on-LAN and TrueNAS actions via Telegram API without exposing ports.
          </span>
        </div>
        <div style={{ display: 'flex', gap: 4, marginTop: 8 }}>
          {['ESP32', 'C++', 'Python', 'Telegram API'].map(t => (
            <span key={t} style={{ fontSize: 9, fontWeight: 600, color: '#94a3b8', background: 'rgba(255,255,255,0.04)', padding: '2px 6px', borderRadius: 4 }}>{t}</span>
          ))}
        </div>
      </div>

      <div style={{
        display: 'flex', flexDirection: 'column', flex: 1, padding: 14,
        background: 'rgba(255,255,255,0.01)', border: '1px solid rgba(255,255,255,0.04)', borderRadius: 10,
        justifyContent: 'space-between'
      }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ fontSize: 13, fontWeight: 700, color: '#ffffff' }}>GradeWise</span>
            <span style={{ fontSize: 10, fontWeight: 600, color: '#06b6d4', background: 'rgba(6,182,212,0.08)', padding: '2px 6px', borderRadius: 4 }}>Full-Stack AI</span>
          </div>
          <span style={{ fontSize: 11, color: '#cbd5e1', lineHeight: 1.4 }}>
            AI-powered grading tool that extracts questions from student papers and generates structured feedback.
          </span>
        </div>
        <div style={{ display: 'flex', gap: 4, marginTop: 8 }}>
          {['Next.js', 'React', 'Genkit', 'Google Cloud'].map(t => (
            <span key={t} style={{ fontSize: 9, fontWeight: 600, color: '#94a3b8', background: 'rgba(255,255,255,0.04)', padding: '2px 6px', borderRadius: 4 }}>{t}</span>
          ))}
        </div>
      </div>
    </div>
  </div>
</div>
```

<br/>

```aura width=850 height=220
<div style={{
  width: '100%', height: '100%', background: '#09090e',
  display: 'flex', padding: '24px', fontFamily: 'Inter, sans-serif', borderRadius: 16,
  border: '1px solid rgba(255, 255, 255, 0.05)', alignItems: 'center'
}}>
  <div style={{ display: 'flex', flexDirection: 'column', width: '45%', paddingRight: 24, borderRight: '1px solid rgba(255,255,255,0.06)' }}>
    <span style={{ fontSize: 13, fontWeight: 800, color: '#818cf8', letterSpacing: '0.5px', textTransform: 'uppercase', marginBottom: 16 }}>
      📈 GitHub Analytics
    </span>
    <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
      <div style={{ display: 'flex', gap: 10 }}>
        <div style={{ display: 'flex', flexDirection: 'column', flex: 1, padding: '10px 14px', background: 'rgba(255,255,255,0.01)', border: '1px solid rgba(255,255,255,0.03)', borderRadius: 8 }}>
          <span style={{ fontSize: 10, fontWeight: 500, color: '#94a3b8' }}>Commits</span>
          <span style={{ fontSize: 18, fontWeight: 800, color: '#ffffff', marginTop: 2 }}>{github?.stats?.totalCommits ?? 1547}</span>
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', flex: 1, padding: '10px 14px', background: 'rgba(255,255,255,0.01)', border: '1px solid rgba(255,255,255,0.03)', borderRadius: 8 }}>
          <span style={{ fontSize: 10, fontWeight: 500, color: '#94a3b8' }}>Stars Received</span>
          <span style={{ fontSize: 18, fontWeight: 800, color: '#fbbf24', marginTop: 2 }}>{github?.stats?.totalStars ?? 128}</span>
        </div>
      </div>
      <div style={{ display: 'flex', gap: 10 }}>
        <div style={{ display: 'flex', flexDirection: 'column', flex: 1, padding: '10px 14px', background: 'rgba(255,255,255,0.01)', border: '1px solid rgba(255,255,255,0.03)', borderRadius: 8 }}>
          <span style={{ fontSize: 10, fontWeight: 500, color: '#94a3b8' }}>Forks</span>
          <span style={{ fontSize: 18, fontWeight: 800, color: '#38bdf8', marginTop: 2 }}>{github?.stats?.totalForks ?? 34}</span>
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', flex: 1, padding: '10px 14px', background: 'rgba(255,255,255,0.01)', border: '1px solid rgba(255,255,255,0.03)', borderRadius: 8 }}>
          <span style={{ fontSize: 10, fontWeight: 500, color: '#94a3b8' }}>Repositories</span>
          <span style={{ fontSize: 18, fontWeight: 800, color: '#34d399', marginTop: 2 }}>{github?.stats?.totalRepos ?? 25}</span>
        </div>
      </div>
    </div>
  </div>

  <div style={{ display: 'flex', flexDirection: 'column', width: '55%', paddingLeft: 24 }}>
    <span style={{ fontSize: 13, fontWeight: 800, color: '#818cf8', letterSpacing: '0.5px', textTransform: 'uppercase', marginBottom: 12 }}>
      🧠 Language Distribution
    </span>
    
    <div style={{ display: 'flex', width: '100%', height: 12, borderRadius: 6, overflow: 'hidden', backgroundColor: 'rgba(255,255,255,0.05)', marginBottom: 16 }}>
      {((github && github.languages && github.languages.length > 0) ? github.languages.slice(0, 5) : [
        { name: 'TypeScript', percentage: 45, color: '#3178c6' },
        { name: 'JavaScript', percentage: 25, color: '#f1e05a' },
        { name: 'Python', percentage: 15, color: '#3572A5' },
        { name: 'C++', percentage: 10, color: '#f34b7d' },
        { name: 'Other', percentage: 5, color: '#858585' }
      ]).map((l) => (
        <div key={l.name} style={{ width: `${l.percentage}%`, height: '100%', backgroundColor: l.color ?? '#858585' }} />
      ))}
    </div>

    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px 16px' }}>
      {((github && github.languages && github.languages.length > 0) ? github.languages.slice(0, 5) : [
        { name: 'TypeScript', percentage: 45, color: '#3178c6' },
        { name: 'JavaScript', percentage: 25, color: '#f1e05a' },
        { name: 'Python', percentage: 15, color: '#3572A5' },
        { name: 'C++', percentage: 10, color: '#f34b7d' },
        { name: 'Other', percentage: 5, color: '#858585' }
      ]).map((l) => (
        <div key={l.name} style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
          <div style={{ width: 8, height: 8, borderRadius: 4, backgroundColor: l.color ?? '#858585' }} />
          <span style={{ fontSize: 11, fontWeight: 600, color: '#cbd5e1' }}>{l.name}</span>
          <span style={{ fontSize: 11, color: '#94a3b8' }}>{l.percentage}%</span>
        </div>
      ))}
    </div>
  </div>
</div>
```

<br/>

<div align="center">
  <i>"Simplicity is the ultimate sophistication."</i><br><br>
  <a href="https://linkedin.com/in/divyanshjoshidev">Let's connect and build something awesome together! 🚀</a>
</div>
