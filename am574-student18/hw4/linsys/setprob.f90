subroutine setprob

    implicit none
    character*25 :: fname
    integer :: iunit
    real(kind=8) :: a11,a12,a21,a22

    common /cparam/ a11,a12,a21,a22   
 
    ! Set the material parameters for this linear system
    ! Passed to the Riemann solver rp1.f in a common block
 
    iunit = 4
    fname = 'setprob.data'
    ! open the unit with new routine from Clawpack 4.4 to skip over
    ! comment lines starting with #:
    call opendatafile(iunit, fname)


    ! compoenents of matrix A
    read(4,*) a11

    read(4,*) a12

    read(4,*) a21

    read(4,*) a22

end subroutine setprob
