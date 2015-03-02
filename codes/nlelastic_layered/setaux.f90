subroutine setaux(mbc,mx,xlower,dx,maux,aux)

    ! Called at start of computation before calling qinit, and
    ! when AMR is used, also called every time a new grid patch is created.
    ! Use to set auxiliary arrays aux(1:maux, 1-mbc:mx+mbc, 1-mbc:my+mbc).
    ! Note that ghost cell values may need to be set if the aux arrays
    ! are used by the Riemann solver(s).
    !
    ! This default version does nothing. 
 
    implicit none
    integer, intent(in) :: mbc,mx,maux
    real(kind=8), intent(in) :: xlower,dx
    real(kind=8), intent(out) ::  aux(maux,1-mbc:mx+mbc)
    
    REAL, PARAMETER :: Pi = 3.1415926535
    real(kind=8) :: xcell
    integer :: i
    
      do i=1,mx
         xcell = xlower + (i-0.5d0)*dx
	 aux(1,i) = 2 - sin(Pi*xcell)
      enddo
      aux(1,0)=aux(1,1)
      aux(1,-1)=aux(1,1)
      aux(1,mx+mbc)=aux(1,mx+mbc-2)
      aux(1,mx+mbc-1)=aux(1,mx+mbc-2)
      


end subroutine setaux
