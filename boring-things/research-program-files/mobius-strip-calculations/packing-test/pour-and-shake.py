import pybullet as p, numpy as np, sys, time
L=2*np.pi; W=0.5; T=0.08; R=1.0; NS=24
def frames(kind):
    if kind=='straight': return [((0,0,0),(0,0,0,1),(L/2,W/2,T/2))]
    out=[]; seg=2*np.pi*(R+W/2)/NS*1.03
    for i in range(NS):
        u=2*np.pi*i/NS
        if kind=='ring': wv=np.array([np.cos(u),np.sin(u),0.])
        else:
            a=kind*u/2; wv=np.array([np.sin(a)*np.cos(u),np.sin(a)*np.sin(u),np.cos(a)])
        t=np.array([-np.sin(u),np.cos(u),0.]); n=np.cross(t,wv)
        M=np.c_[t,wv,n]
        # rotation matrix to quaternion
        tr=np.trace(M)
        if tr>0:
            s=np.sqrt(tr+1)*2; q=((M[2,1]-M[1,2])/s,(M[0,2]-M[2,0])/s,(M[1,0]-M[0,1])/s,s/4)
        else:
            i0=int(np.argmax(np.diag(M))); j=(i0+1)%3; k=(i0+2)%3
            s=np.sqrt(1+M[i0,i0]-M[j,j]-M[k,k])*2; q=[0,0,0,0]
            q[i0]=s/4; q[j]=(M[j,i0]+M[i0,j])/s; q[k]=(M[k,i0]+M[i0,k])/s; q[3]=(M[k,j]-M[j,k])/s; q=tuple(q)
        out.append((tuple(R*np.array([np.cos(u),np.sin(u),0.])),q,(seg/2,W/2,T/2)))
    return out
def run(kind,S,seed,verbose=False):
    rng=np.random.default_rng(seed)
    p.connect(p.DIRECT); p.setGravity(0,0,-9.8); p.setPhysicsEngineParameter(numSolverIterations=12,fixedTimeStep=1/240.)
    H=4*S+12; w=1.0
    def wall(pos,he):
        c=p.createCollisionShape(p.GEOM_BOX,halfExtents=he); b=p.createMultiBody(0,c,basePosition=pos); p.changeDynamics(b,-1,lateralFriction=0.3)
    wall((S/2,S/2,-w),(S/2+w,S/2+w,w)); wall((-w,S/2,H/2),(w,S/2+w,H/2)); wall((S+w,S/2,H/2),(w,S/2+w,H/2)); wall((S/2,-w,H/2),(S/2+w,w,H/2)); wall((S/2,S+w,H/2),(S/2+w,w,H/2))
    fr=frames(kind)
    col=p.createCollisionShapeArray([p.GEOM_BOX]*len(fr),halfExtents=[f[2] for f in fr],collisionFramePositions=[f[0] for f in fr],collisionFrameOrientations=[f[1] for f in fr])
    ext=L/2 if kind=='straight' else R+W/2
    bodies=[]
    def top():
        return max([p.getBasePositionAndOrientation(b)[0][2] for b in bodies],default=0)
    def step(sec):
        for _ in range(int(sec*240)): p.stepSimulation()
    def pour(n):
        z=top()+ext+1.0
        for i in range(n):
            q=rng.normal(size=4); q/=np.linalg.norm(q)
            m=min(ext,S/2-0.05)
            pos=(rng.uniform(m,S-m),rng.uniform(m,S-m),z+i*0.9)
            b=p.createMultiBody(1.0,col,basePosition=pos,baseOrientation=q.tolist())
            p.changeDynamics(b,-1,lateralFriction=0.3,restitution=0.0,linearDamping=0.05,angularDamping=0.05)
            bodies.append(b)
        step(1.2+n*0.9/6)
    def jostle(sec=4.0,amp=1.5):
        n=int(sec/0.2)
        for k in range(n):
            a=amp*(1-k/n)
            for b in bodies:
                v,wv=p.getBaseVelocity(b)
                p.resetBaseVelocity(b,(v[0]+rng.normal()*a,v[1]+rng.normal()*a,v[2]+abs(rng.normal())*a*0.6),(wv[0]+rng.normal()*a,wv[1]+rng.normal()*a,wv[2]+rng.normal()*a))
            step(0.2)
        step(2.0)
    loc=np.array([[x,0,0] for x in np.linspace(-L/2,L/2,NS)]) if kind=='straight' else np.array([f[0] for f in fr])
    def inside():
        # amount of strip below the rim counted in whole strips (24 sample points along each strip)
        tot=0
        for b in bodies:
            pos,q=p.getBasePositionAndOrientation(b); M=np.array(p.getMatrixFromQuaternion(q)).reshape(3,3)
            tot+=((loc@M.T)[:,2]+pos[2]<S).sum()
        return tot/NS
    def pen():
        d=[c[8] for c in p.getContactPoints()]
        return (round(float(np.percentile(d,1)),3),round(float(np.min(d)),3)) if d else (0,0)
    batch=max(4,int(S*S/3))
    t0=time.time(); before=None
    for rounds in range(400):
        pour(batch)
        if len(bodies)-inside()>=max(3,batch//2):
            if before is None: before=inside()
            jostle()
            if len(bodies)-inside()>=3: break
        if time.time()-t0>2400: break
    step(1.5)
    res=(round(before,1) if before else None,round(inside(),1),len(bodies),pen(),round(time.time()-t0))
    p.disconnect(); return res
if __name__=='__main__':
    kind=sys.argv[1]; kind=int(kind) if kind.isdigit() else kind
    print(kind,sys.argv[2],run(kind,float(sys.argv[2]),int(sys.argv[3])),flush=True)
