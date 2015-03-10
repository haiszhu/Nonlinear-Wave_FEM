! =====================================================
subroutine rp1(maxm,meqn,mwaves,maux,mbc,mx,ql,qr,auxl,auxr,fwave,s,amdq,apdq)
! =====================================================

! Riemann solver for the nonlinear elastic equations in 1d,
!  variable coefficients
!   eps_t - (m/rho(x))_x = 0
!   m_t - sigma(eps,x)_x =0
! where eps=strain, m=rho*u=momentum
! f-wave is used

! waves:     2
! equations: 2

! Conserved quantities:
!       1 strain
!       2 momentum

! On input, ql contains the state vector at the left edge of each cell
!           qr contains the state vector at the right edge of each cell

! On output, wave contains the waves,
!            s the speeds,
! 
!            amdq = A^- Delta q,
!            apdq = A^+ Delta q,
!                   the decomposition of the flux difference
!                       f(qr(i-1)) - f(ql(i))
!                   into leftgoing and rightgoing parts respectively.
! 

! Note that the i'th Riemann problem has left state qr(i-1,:)
!                                    and right state ql(i,:)
! From the basic clawpack routines, this routine is called with ql = qr


    implicit double precision (a-h,o-z)

    dimension wave(meqn, mwaves, 1-mbc:maxm+mbc)
    dimension    s(mwaves,1-mbc:maxm+mbc)
    dimension   ql(meqn, 1-mbc:maxm+mbc)
    dimension   qr(meqn, 1-mbc:maxm+mbc)
    dimension apdq(meqn, 1-mbc:maxm+mbc)
    dimension amdq(meqn, 1-mbc:maxm+mbc)
    dimension fwave(meqn, mwaves, 1-mbc:maxm+mbc)
    dimension auxl(maux, 1-mbc:maxm+mbc)
    dimension auxr(maux, 1-mbc:maxm+mbc)
    dimension fluxl(meqn, 1-mbc:maxm+mbc)
    dimension fluxr(meqn, 1-mbc:maxm+mbc)

    dimension Z(1-mbc:maxm+mbc)
    dimension C(1-mbc:maxm+mbc)	
!     local arrays
!     ------------
    dimension delta(2)

!     # density, bulk modulus, and sound speed, and impedence of medium:
!     # (should be set in setprob.f)
    common /cparam/ rho,bulk,cc,zz


!     # split the jump in q at each interface into waves

!     # find a1 and a2, the coefficients of the 2 eigenvectors:
        
        do 10 i = 1-mbc, mx+mbc
        
!quardratic
!        C(i)=sqrt(1+0.6*ql(1,i)*auxl(1,i))
!exp
	C(i)=sqrt(exp(ql(1,i)*auxl(1,i)))
        Z(i)=C(i)*auxl(1,i)
!        write(*,*) (Z(i))
        
        10 END DO
        
        do 20 i = 2-mbc, mx+mbc
        
        fluxl(1,i) = -ql(2,i)/auxl(1,i)
!quadratic
!	fluxl(2,i)   = -(ql(1,i)*auxl(1,i))-0.5*(ql(1,i)*auxl(1,i))**2
!exp
        fluxl(2,i)   = -(exp(ql(1,i)*auxl(1,i))-1)
        
        fluxr(1,i-1) = -qr(2,i-1)/auxr(1,i-1)
!quadratic
!       fluxr(2,i-1) = -(qr(1,i-1)*auxr(1,i-1))-0.5*(qr(1,i-1)*auxr(1,i-1))**2
!exp
        fluxr(2,i-1) = -(exp(qr(1,i-1)*auxr(1,i-1))-1)
                
        delta(1) = (fluxl(1,i) - fluxr(1,i-1))
        delta(2) = (fluxl(2,i) - fluxr(2,i-1))

	a1= (delta(2)+Z(i)*delta(1))/(Z(i-1)+Z(i))

	a2= (-delta(2)+Z(i-1)*delta(1))/(Z(i-1)+Z(i))
    
    !        # Compute the waves.
    
        fwave(1,1,i) = a1*1
        fwave(2,1,i) = a1*Z(i-1)
        s(1,i) = -C(i-1)

    
        fwave(1,2,i) = a2*1
        fwave(2,2,i) = a2*(-Z(i))
        s(2,i) = C(i)
    
    20 END DO


!     # compute the leftgoing and rightgoing flux differences:
!     # Note s(1,i) < 0   and   s(2,i) > 0.

    do 220 m=1,meqn
        do 220 i = 2-mbc, mx+mbc
            amdq(m,i) = fwave(m,1,i)
            apdq(m,i) = fwave(m,2,i)
    220 END DO

    return
    end subroutine rp1
