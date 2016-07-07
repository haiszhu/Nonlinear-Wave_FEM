c
c
c =========================================================
       subroutine qinit(meqn,mbc,mx,xlower,dx,q,maux,aux)
c =========================================================
c
c     # Set initial conditions for q.
c
c
      implicit double precision (a-h,o-z)
      dimension q(meqn,1-mbc:mx+mbc)
      dimension aux(maux,1-mbc:mx+mbc)
      common /comic/ beta
c
c
      pi2 = 8.d0*datan(1.d0)  !# = 2 * pi
      do 150 i=1,mx
         xcell = xlower + (i-0.5d0)*dx
         q(1,i) = 1.d0
c         q(1,i) = 0.01d0   
         if (xcell.gt.0.d0 .and. xcell.lt.1.d0) then
             q(1,i) = 4.d0
             endif
  150    continue
c
      return
      end

