from flask import Flask, request, jsonify
from nlp_engine import analyze_payload
import subprocess
import json

app = Flask(__name__)

def check_snort_logs(target_ip):
    """
    Parses local Snort alert logs to see if a deterministic rule fired.
    """
    try:
        # Grep the snort alert file for the specific IP (Simplified for the lab)
        result = subprocess.run(['grep', target_ip, '/var/log/snort/alert'], capture_output=True, text=True)
        if result.stdout:
            return {"detected": True, "details": "Signature match found in Snort baseline."}
    except Exception as e:
        pass
    return {"detected": False, "details": "No signature match."}

@app.route('/api/analyze', methods=['POST'])
def analyze_threat():
    data = request.get_json()
    
    if not data or 'payload' not in data or 'target_ip' not in data:
        return jsonify({"error": "Missing payload or target_ip"}), 400
        
    payload = data['payload']
    target_ip = data['target_ip']
    
    # 1. Deterministic Engine Check (Snort)
    snort_result = check_snort_logs(target_ip)
    
    # 2. Heuristic Engine Check (NLP)
    nlp_result = analyze_payload(payload)
    
    # Consensus Mechanism
    is_threat = snort_result['detected'] or nlp_result['is_malicious']
    
    response = {
        "status": "success",
        "verdict": "MALICIOUS" if is_threat else "BENIGN",
        "engines": {
            "snort": snort_result,
            "nlp_heuristic": nlp_result
        },
        "payload_length": len(payload)
    }
    
    return jsonify(response), 200

if __name__ == '__main__':
    # Running on port 5000, optimized for micro-instances
    app.run(host='0.0.0.0', port=5000, threaded=True)