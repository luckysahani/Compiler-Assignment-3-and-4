.text
main:    #assume value a is already in $t0, b in $t1
	li	$t0,10
	li	$t1,15
    add $a0,$0,$t0   # it's same function as move the value
    add $a1,$0,$t1 
    jal addThem     # call procedure
    add $t3,$0,$v0   # move the return value from $v0 to where we want
    move $a0,$t3
    li $v0,1
    syscall
    li $v0,10
    syscall

addThem:
    addi $sp,$sp,-4     # Moving Stack pointer
    sw $t0, 0($sp)      # Store previous value

    add $t0,$a0,$a1     # Procedure Body
    add $v0,$0,$t0      # Result

    lw $t0, 0($sp)      # Load previous value
    addi $sp,$sp,4      # Moveing Stack pointer 
    jr $ra              # return (Copy $ra to PC)