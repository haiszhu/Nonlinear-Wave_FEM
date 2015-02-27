! =====================================================
subroutine rp1(maxm,meqn,mwaves,maux,mbc,mx,ql,qr,auxl,auxr,wave,s,amdq,apdq)
! =====================================================

! Riemann solver for elastic waves.

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

!     local arrays
!     ------------
    dimension delta(2)

!     # xlower, xupper, num_cells:
!     # (should be set in setprob.f)
!    common /cparam/ xlower, xupper, numcells
    common /cparam/ xlower, dx

!     # cell length
!    dx = (xupper - xlower)/numcells


!     # split the jump in q at each interface into waves

!     # find a1 and a2, the coefficients of the 2 eigenvectors:
    do 20 i = 2-mbc, mx+mbc
	
	xcell = xlower + (i+0.5d0)*dx	!# check xcell stands for center of which cell
	xcellm = xcell - 1.d0*dx
!	print *, xlower, dx	!# insure paramenter right (3 parameters will have issue)

	rhoi = rho(xcell)
	rhoim = rho(xcellm)
	epsi = ql(1,i)
	epsim = qr(1,i-1)
	urhoi = ql(2,i)
	urhoim = qr(2,i-1)

!       # compute wave speeds

	bulki = sigmap(epsi,xcell)
	bulkim = sigmap(epsim,xcellm)
	ci = dsqrt(bulki / rhoi)
	cim = dsqrt(bulkim / rhoim)	
 
!       # compute eigenvector compunents
	zi = rhoi*ci
	zim = rhoim*cim

!	# decompose flux difference
	dq1 = urhoim/rhoim - urhoi/rhoi
	dq2 = sigma(epsim,xcell) - sigma(epsi,xcellm)
	a1 = (zi*dq1 + dq2) / (zi + zim)
	a2 = (zim*dq1 - dq2) / (zi + zim)

!       # compute fwaves

	wave(1,1,i) = a1
	wave(2,1,i) = a1*zim
	s(1,i) = -cim

	wave(1,2,i) = a2
	wave(2,2,i) = -a2*zi
	s(2,i) = ci
	
    
    20 END DO


!     # compute the leftgoing and rightgoing flux differences:
!     # Note s(1,i) < 0   and   s(2,i) > 0.

    do 220 m=1,meqn
        do 220 i = 2-mbc, mx+mbc
            amdq(m,i) = wave(m,1,i)
            apdq(m,i) = wave(m,2,i)
    220 END DO

    return
    end subroutine rp1


!     --------------------------------------------
      double precision function rho(xcell)
!     --------------------------------------------
      implicit double precision (a-h,o-z)

!     # density in ith cell

!	# spacially varying case (not ready)        
!	pi = 4.d0 * datan(1.d0)  !# = pi
!	xi = 
!        rho = 2.d0 - dsin(pi*xi)

!	# alternating layer case
	ix = floor(xcell)
	xfrac = xcell - ix
	if (xfrac .lt. 0.5d0) then
!	    # layer A:
	    rho = 4.d0
!	    rho = 1.d0	!# for test
	else
!	    # layer B:
	    rho = 1.d0
	endif

!	# constant case
!	rho = 1.d0

      return
      end


!     --------------------------------------------
      double precision function sigma(eps,xcell)
!     --------------------------------------------
      implicit double precision (a-h,o-z)

!     # stress-strain relation in ith cell
 
!	# spacially varying case (not ready)          
!	pi = 4.d0 * datan(1.d0)  !# = pi
!	xi = 
!        sigma = eps*(2-dsin(pi*xi)) + 0.3d0*(eps*(2-dsin(pi*xi)))**2 

!	# alternating layer case
	ix = floor(xcell)
	xfrac = xcell - ix
	if (xfrac .lt. 0.5d0) then
!	    # layer A:
	    sigma = 0.25d0 * eps
!	    sigma = 1.d0 * eps	!# for test
	else
!	    # layer B:
	    sigma = 1.d0 * eps
	endif

!	# constant case
!	sigma = 1.d0*eps
      return
      end


!     --------------------------------------------
      double precision function sigmap(eps,xcell)
!     --------------------------------------------
      implicit double precision (a-h,o-z)

!     # derivative of stress-strain relation in ith cell

!	# spacially varying case (not ready) 	
!	pi = 4.d0*datan(1.d0)  !# = pi
!	xi = 
!        sigmap = -eps*pi*dcos(pi*xi) - 0.6d0*eps*(2-dsin(pi*xi))*pi*dcos(pi*xi)

!	# alternating layer case
	ix = floor(xcell)
	xfrac = xcell - ix
	if (xfrac .lt. 0.5d0) then
!	    # layer A:
	    sigmap = 0.25d0
!	    sigmap = 1.d0	!# for test
	else
!	    # layer B:
	    sigmap = 1.d0 
	endif

!	# constant case
!	sigmap = 1.d0
      return
      end
