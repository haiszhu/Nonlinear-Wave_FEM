! =============================================================================
subroutine rp1(maxmx,meqn,mwaves,maux,mbc,mx,ql,qr,auxl,auxr,wave,s,amdq,apdq)
! =============================================================================
!
! Riemann problems for the 1D Burgers' equation without entropy fix for 
! transonic rarefaction. See "Finite Volume Method for Hyperbolic Problems",
! R. J. LeVeque.

! waves: 1
! equations: 1

! Conserved quantities:
!       1 q
    
    implicit double precision (a-h,o-z)

    integer :: maxmx, meqn, mwaves, mbc, mx
        
    double precision :: ql(meqn,1-mbc:maxmx+mbc)
    double precision :: qr(meqn,1-mbc:maxmx+mbc)
    double precision :: s(mwaves, 1-mbc:maxmx+mbc)
    double precision :: wave(meqn, mwaves, 1-mbc:maxmx+mbc)
    double precision :: amdq(meqn, 1-mbc:maxmx+mbc)
    double precision :: apdq(meqn, 1-mbc:maxmx+mbc)
    integer :: i
    logical :: efix
 
    efix = .false.   !# Compute correct flux for transonic rarefactions
 

    do i=2-mbc,mx+mbc
        wave(1,1,i) = ql(1,i)**0.5d0 - qr(1,i-1)**0.5d0
	    
	    if (wave(1,1,i).eq.0.d0) then
	        s(1,i) = 0.5d0*ql(1,i)**(-0.5d0)
	    else
	        s(1,i) = wave(1,1,i)/(ql(1,i)-qr(1,i-1))	
	    endif

        amdq(1,i) = dmin1(dsign(1.d0, s(1,i)), 0.d0) * wave(1,1,i)
        apdq(1,i) = dmax1(dsign(1.d0, s(1,i)), 0.d0) * wave(1,1,i)

    enddo

    return
    end subroutine
