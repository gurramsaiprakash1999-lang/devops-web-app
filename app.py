from flask import Flask, render_template_string
import platform
import socket
import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cloud Hub Portal</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #0f172a;
            color: #f8fafc;
            font-family: 'Segoe UI', Roboto, sans-serif;
            min-height: 100vh;
        }
        .navbar-brand {
            font-weight: 700;
            font-size: 1.5rem;
            background: linear-gradient(135deg, #38bdf8, #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .card-custom {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 12px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }
        .card-custom:hover {
            transform: translateY(-4px);
            border-color: #38bdf8;
        }
        .status-badge {
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            background: rgba(34, 197, 94, 0.2);
            color: #4ade80;
            border: 1px solid #22c55e;
        }
        .tech-icon {
            font-size: 2rem;
            margin-bottom: 10px;
        }
        .hero-title {
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #60a5fa, #a78bfa, #f472b6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg border-bottom border-secondary mb-4 py-3">
        <div class="container">
            <a class="navbar-brand" href="#"><i class="fa-solid fa-cloud"></i> CLOUD HUB APPLICATION</a>
            <span class="status-badge"><i class="fa-solid fa-circle-check"></i> System Operational</span>
        </div>
    </nav>

    <div class="container pb-5">
        <div class="text-center mb-5">
            <h1 class="hero-title">Welcome to Cloud Hub Portal</h1>
            <p class="text-secondary fs-5">Automated Multi-Cloud Infrastructure & DevOps Dashboard</p>
        </div>

        <!-- Server Metrics Grid -->
        <div class="row g-4 mb-5">
            <div class="col-md-4">
                <div class="card-custom p-4">
                    <div class="tech-icon text-info"><i class="fa-solid fa-server"></i></div>
                    <h5 class="text-secondary">Host OS & Arch</h5>
                    <h4 class="fw-bold">{{ system_info.os }}</h4>
                    <p class="mb-0 text-muted">Node: {{ system_info.hostname }}</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card-custom p-4">
                    <div class="tech-icon text-warning"><i class="fa-solid fa-network-wired"></i></div>
                    <h5 class="text-secondary">Pod Container IP</h5>
                    <h4 class="fw-bold">{{ system_info.ip }}</h4>
                    <p class="mb-0 text-muted">Kubernetes Pod Network</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card-custom p-4">
                    <div class="tech-icon text-success"><i class="fa-solid fa-clock"></i></div>
                    <h5 class="text-secondary">Container Time (UTC)</h5>
                    <h4 class="fw-bold">{{ system_info.time }}</h4>
                    <p class="mb-0 text-muted">Live Runtime Status</p>
                </div>
            </div>
        </div>

        <!-- Infrastructure Stack Section -->
        <h4 class="fw-bold mb-3"><i class="fa-solid fa-cubes"></i> Integrated Cloud Stack</h4>
        <div class="row g-3">
            <div class="col-6 col-md-2">
                <div class="card-custom p-3 text-center">
                    <i class="fa-brands fa-github fa-2x text-light mb-2"></i>
                    <h6>GitHub</h6>
                </div>
            </div>
            <div class="col-6 col-md-2">
                <div class="card-custom p-3 text-center">
                    <i class="fa-solid fa-layer-group fa-2x text-primary mb-2"></i>
                    <h6>Terraform</h6>
                </div>
            </div>
            <div class="col-6 col-md-2">
                <div class="card-custom p-3 text-center">
                    <i class="fa-solid fa-gears fa-2x text-danger mb-2"></i>
                    <h6>Ansible</h6>
                </div>
            </div>
            <div class="col-6 col-md-2">
                <div class="card-custom p-3 text-center">
                    <i class="fa-brands fa-docker fa-2x text-info mb-2"></i>
                    <h6>Docker</h6>
                </div>
            </div>
            <div class="col-6 col-md-2">
                <div class="card-custom p-3 text-center">
                    <i class="fa-solid fa-dharmachakra fa-2x text-primary mb-2"></i>
                    <h6>Kubernetes</h6>
                </div>
            </div>
            <div class="col-6 col-md-2">
                <div class="card-custom p-3 text-center">
                    <i class="fa-brands fa-jenkins fa-2x text-warning mb-2"></i>
                    <h6>Jenkins (Java 21)</h6>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def cloud_hub():
    info = {
        'os': f"{platform.system()} {platform.release()}",
        'hostname': socket.gethostname(),
        'ip': socket.gethostbyname(socket.gethostname()),
        'time': datetime.datetime.now().strftime("%H:%M:%S")
    }
    return render_template_string(HTML_TEMPLATE, system_info=info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
