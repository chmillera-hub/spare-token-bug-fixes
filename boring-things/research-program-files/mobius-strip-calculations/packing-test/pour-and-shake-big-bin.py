import pybullet as p, numpy as np, sys, time
L=2*np.pi; W=0.5; T=0.08; R=1.0; NS=24
def quat(M):
    tr=np.trace(M)
    if tr>0:
        s=np.sqrt(tr+1)*2; return ((M[2,1]-M[1,2])/s,(M[0,2]-M[2,0])/s,(M[1,0]-M[0,1])/s,s/4)
    i0=int(np.argmax(np.diag(M))); j=(i0+1)%3; k=(i0+2)%3
    s=np.sqrt(1+M[i0,i0]-M[j,j]-M[k,k])*2; q=[0,0,0,0]
    q[i0]=s/4; q[j]=(M[j,i0]+M[i0,j])/s; q[k]=(M[k,i0]+M[i0,k])/s; q[3]=(M[k,j]-M[j,k])/s; return tuple(q)
def frames(kind):
    # returns list of (position, quaternion, half extents) and 24 sample points along the strip
    if kind=='straight':
        return [((0,0,0),(0,0,0,1),(L/2,W/2,T/2))], np.array([[x,0,0] for x in np.linspace(-L/2,L/2,NS)])
    if kind=='vfold':
        c=np.array([L/8,0,L/8])
        Mz=np.array([[0,0,1.],[0,1,0],[-1,0,0]]).T  # box x axis points along world z
        fr=[(tuple(np.array([L/4,0,0])-c),(0,0,0,1),(L/4,W/2,T/2)),(tuple(np.array([0,0,L/4])-c),quat(np.array([[0,0,-1.],[0,1,0],[1,0,0]])),(L/4,W/2,T/2))]
        pts=np.array([[x,0,0] for x in np.linspace(0,L/2,NS//2)]+[[0,0,z] for z in np.linspace(0,L/2,NS//2)])-c
        return fr,pts
    out=[]
    if kind=='arc':
        R2=2.0; cen=np.array([0,2*R2/np.pi,0]); seg=np.pi*(R2+W/2)/NS*1.03
        for i in range(NS):
            u=np.pi*(i+0.5)/NS; wv=np.array([np.cos(u),np.sin(u),0.]); t=np.array([-np.sin(u),np.cos(u),0.]); n=np.cross(t,wv)
            out.append((tuple(R2*wv-cen),quat(np.c_[t,wv,n]),(seg/2,W/2,T/2)))
        return out,np.array([f[0] for f in out])
    seg=2*np.pi*(R+W/2)/NS*1.03
    for i in range(NS):
        u=2*np.pi*i/NS
        if kind=='ring': wv=np.array([np.cos(u),np.sin(u),0.])
        else:
            a=kind*u/2; wv=np.array([np.sin(a)*np.cos(u),np.sin(a)*np.sin(u),np.cos(a)])
        t=np.array([-np.sin(u),np.cos(u),0.]); n=np.cross(t,wv)
        out.append((tuple(R*np.array([np.cos(u),np.sin(u),0.])),quat(np.c_[t,wv,n]),(seg/2,W/2,T/2)))
    return out,np.array([f[0] for f in out])
def run(kinds,S,seed,tcap):
    rng=np.random.default_rng(seed)
    p.connect(p.DIRECT); p.setGravity(0,0,-9.8)
    fine=any(k in ('straight','vfold','arc') for k in kinds)
    p.setPhysicsEngineParameter(numSolverIterations=(25 if fine else 12),fixedTimeStep=1/240.,numSubSteps=(2 if fine else 1))
    H=4*S+12; w=1.0
    def wall(pos,he):
        c=p.createCollisionShape(p.GEOM_BOX,halfExtents=he); b=p.createMultiBody(0,c,basePosition=pos); p.changeDynamics(b,-1,lateralFriction=0.3)
    wall((S/2,S/2,-w),(S/2+w,S/2+w,w)); wall((-w,S/2,H/2),(w,S/2+w,H/2)); wall((S+w,S/2,H/2),(w,S/2+w,H/2)); wall((S/2,-w,H/2),(S/2+w,w,H/2)); wall((S/2,S+w,H/2),(S/2+w,w,H/2))
    info={}
    for k in kinds:
        fr,loc=frames(k)
        col=p.createCollisionShapeArray([p.GEOM_BOX]*len(fr),halfExtents=[f[2] for f in fr],collisionFramePositions=[f[0] for f in fr],collisionFrameOrientations=[f[1] for f in fr])
        ext=max(np.linalg.norm(np.array(f[0]))+np.linalg.norm(f[2]) for f in fr) if k in('vfold','arc') else (L/2 if k=='straight' else R+W/2)
        info[k]=(col,loc,ext)
    bodies=[]  # (id, kind)
    def top(): return max([p.getBasePositionAndOrientation(b)[0][2] for b,_ in bodies],default=0)
    def step(sec):
        for _ in range(int(sec*240)): p.stepSimulation()
    def add(k,pos,q):
        b=p.createMultiBody(1.0,info[k][0],basePosition=pos,baseOrientation=q)
        p.changeDynamics(b,-1,lateralFriction=0.3,restitution=0.0,linearDamping=0.05,angularDamping=0.05); bodies.append((b,k))
    def pour(k,n,z):
        col,loc,ext=info[k]
        if k=='straight':
            m=8; i=0; lay=0
            while i<n:
                yaw=rng.uniform(0,np.pi); u=np.array([np.cos(yaw),np.sin(yaw)]); v=np.array([-u[1],u[0]])
                for j in range(m):
                    if i>=n: break
                    q=p.getQuaternionFromEuler((rng.uniform(0,2*np.pi),rng.uniform(-0.35,0.35),yaw))
                    c=np.array([S/2,S/2])+v*(j-(m-1)/2)*0.95+u*rng.uniform(-1.0,1.0)
                    # keep the strip inside the walls
                    hx=abs(u[0])*L/2+0.3; hy=abs(u[1])*L/2+0.3
                    c[0]=min(max(c[0],hx),S-hx); c[1]=min(max(c[1],hy),S-hy)
                    add(k,(c[0],c[1],z+1.2+lay*2.3),q); i+=1
                lay+=1
            return z+1.2+lay*2.3
        g=max(1,int(S//(2*ext+0.15))); cell=S/g; i=0; lay=0
        cells=[(a,c) for a in range(g) for c in range(g)]
        while i<n:
            rng.shuffle(cells)
            for a,c in cells:
                if i>=n: break
                q=rng.normal(size=4); q/=np.linalg.norm(q)
                add(k,((a+0.5)*cell,(c+0.5)*cell,z+ext+lay*(2*ext+0.15)),q.tolist()); i+=1
            lay+=1
        return z+lay*(2*ext+0.15)
    def count(region):
        tot={k:0 for k in kinds}
        for b,k in bodies:
            pos,q=p.getBasePositionAndOrientation(b); M=np.array(p.getMatrixFromQuaternion(q)).reshape(3,3)
            X=info[k][1]@M.T+np.array(pos); tot[k]+=region(X).sum()/len(info[k][1])
        return tot
    m=2.5
    inside=lambda: sum(count(lambda X:X[:,2]<S).values())
    core=lambda: {k:round(v/((S-2*m)**2*(S-4.0)),3) for k,v in count(lambda X:(X[:,0]>m)&(X[:,0]<S-m)&(X[:,1]>m)&(X[:,1]<S-m)&(X[:,2]>1.5)&(X[:,2]<S-2.5)).items()}
    def jostle(sec=4.0,amp=1.5):
        n=int(sec/0.2)
        for j in range(n):
            a=amp*(1-j/n)
            for b,_ in bodies:
                v,wv=p.getBaseVelocity(b)
                p.resetBaseVelocity(b,(v[0]+rng.normal()*a,v[1]+rng.normal()*a,v[2]+abs(rng.normal())*a*0.6),(wv[0]+rng.normal()*a,wv[1]+rng.normal()*a,wv[2]+rng.normal()*a))
            step(0.2)
        step(2.0)
    def nper(k):
        ext=info[k][2]
        if k=='straight': return 16
        g=max(1,int(S//(2*ext+0.15))); return (3 if ext<2 else 1)*g*g
    per=min(nper(k) for k in kinds) if len(kinds)>1 else nper(kinds[0])
    t0=time.time(); r=0
    while True:
        z=top()+0.6; z0=z
        for k in kinds: z=pour(k,per,z)
        step(1.0+0.16*(z-z0)**0.5*2.2)
        r+=1
        if r%5==0: print('progress',kinds,len(bodies),round(top(),1),round(time.time()-t0),file=sys.stderr,flush=True)
        if len(bodies)-inside()>=max(3,per*len(kinds)//3):
            jostle()
            if len(bodies)-inside()>=3: break
        if time.time()-t0>tcap: print('TIME CAP',file=sys.stderr); break
    step(1.5)
    d=[c[8] for c in p.getContactPoints()]
    res=dict(kinds=kinds,S=S,seed=seed,below_rim=round(inside(),1),poured=len(bodies),core=core(),pen=round(float(np.percentile(d,1)),3),secs=round(time.time()-t0))
    p.disconnect(); return res
if __name__=='__main__':
    ks=[int(k) if k.lstrip('-').isdigit() else k for k in sys.argv[1].split('+')]
    print(run(ks,float(sys.argv[2]),int(sys.argv[3]),float(sys.argv[4]) if len(sys.argv)>4 else 5000),flush=True)
