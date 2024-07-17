#import flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "<h1>MINI COOPER</h1><p>The Mini Cooper is a small, iconic British car known for its distinctive design and sporty performance. Initially produced by the British Motor Corporation (BMC) in 1959, it gained fame in the 1960s as an affordable, fuel-efficient vehicle with a unique, compact shape. The original Mini Cooper was designed by Sir Alec Issigonis and later became famous for its racing success under the tuning of John Cooper.In 2001, BMW relaunched the Mini Cooper, preserving its classic style while incorporating modern technology and engineering. The new Mini Coopers are characterized by their nimble handling, compact size, and a range of models including hatchbacks, convertibles, and more performance-oriented versions like the John Cooper Works (JCW).Key features of the Mini Cooper include:* Retro-modern design*Sporty driving dynamics* Customizable options* Advanced safety and infotainment systems* Efficient engines with a blend of performance and fuel economyThe Mini Cooper remains a popular choice for those seeking a stylish, fun-to-drive car with a rich heritage.</p>"

if __name__=='__main__':
    app.run(debug=True)