subroutine setprob

    implicit none
    character*25 :: fname
    integer :: iunit
!    real(kind=8) :: xlower, xupper, numcells
    real(kind=8) :: xlower, dx

!    common /cparam/ xlower, xupper, numcells
    common /cparam/ xlower, dx     
    ! common /cqinit/ beta
 
    ! Set the material parameters for the acoustic equations
    ! Passed to the Riemann solver rp1.f in a common block
 
    iunit = 7
    fname = 'setprob.data'
    ! open the unit with new routine from Clawpack 4.4 to skip over
    ! comment lines starting with #:
    call opendatafile(iunit, fname)


    ! domain:
    read(7,*) xlower

    read(7,*) dx

!    read(7,*) xupper

!    read(7,*) numcells

end subroutine setprob
