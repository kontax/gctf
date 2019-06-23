[bits 64]
; Define variables in the data section
SECTION .DATA
	hello:     db 'Hello world!',10
	helloLen:  equ $-hello

; Code goes in the text section
SECTION .TEXT
	GLOBAL _start 

_start:
	mov rax,4            ; 'write' system call = 4
	mov ebx,1            ; file descriptor 1 = STDOUT
	mov ecx,hello        ; string to write
	mov edx,helloLen     ; length of string to write
	int 80h              ; call the kernel

	; Terminate program
	mov rax,1            ; 'exit' system call
	mov ebx,0            ; exit with error code 0
	int 80h              ; call the kernel

_add:
    pop rcx
    pop rdx
    add rdx, rcx
    push rdx

_sub:
    pop rcx
    pop rdx
    sub rdx, rcx
    push rdx

_multiply:
    pop rcx
    mov rax, rsi
    pop rax
    mul rcx
    push rax
    mov rsi, rax

_divide:

_modulo:

_xor:
    pop rcx
    pop rdx
    xor rdx, rcx

_clone:

_print:

_jmp_top:

jmp

_GOTO_A:
    pop rax
    push rbx
    push rax
    mov rax 389
    push rax
    push rbx
    jmp _GOTO_D

    pop rcx
    pop rdx
    xor rdx, rcx
    push rdx

    jmp _print
label: GOTO_A
pop rax 
push rbx 
push rax 
mov rax 389
    push rax
push rbx
jump_to GOTO_D
xor 
print_top
mov rax 1
    push rax 
add 
pop rbx
if_not_zero 
    jump_to GOTO_A end


label: GOTO_B
pop rax 
push rbx 
push rax 
mov rax 568
    push rax 
push rbx
jump_to GOTO_D
xor 
print_top
mov rax 1
    push rax 
add 
pop rbx
if_not_zero 
    jump_to GOTO_B end


label: GOTO_C
pop rax 
push rbx 
push rax 
mov rax 1023
    push rax 
push rbx
jump_to GOTO_D
xor 
print_top
mov rax 1
    push rax 
add 
pop rbx
if_not_zero 
    jump_to GOTO_C end
exit

label: GOTO_D
mov rax 2
    push rax 
label: GOTO_E
jump_to GOTO_I
label: GOTO_F
if_zero 
    pop_out 
    jump_to GOTO_H end
pop_out 
jump_to GOTO_K

label: GOTO_G
if_zero 
    pop_out 
    jump_to GOTO_H end
pop_out 
pop rax 
mov rbx 1
    push rbx 
sub
if_zero 
    pop_out 
    pop rbx 
    push rax 
    push rbx 
    jump_top end 
push rax
label: GOTO_H
mov rbx 1
    push rbx
add 
jump_to GOTO_E

label: GOTO_I
clone 
mov rax 2
    push rax
label: GOTO_J
sub 
if_zero 
    pop_out 
    mov rax 1
    push rax
    jump_to GOTO_F end
pop_out 
clone 
push rax
modulo 
if_zero 
    jump_to GOTO_F end
pop_out 
clone 
push rax
mov rax 1
    push rax 
add 
clone 
pop rax 
jump_to GOTO_J

label: GOTO_K
clone 
clone 
mov rbx 0
    push rbx
label: GOTO_L
mov rax 10
    push rax
multiply 
pop rbx 
push rax 
modulo
push rbx 
add 
pop rbx 
pop rax 
clone 
push rbx 
sub
if_zero 
    pop_out 
    mov rbx 1
    push rbx 
    jump_to GOTO_G end
pop_out 
push rax 
mov rax 10
    push rax
divide
if_zero 
    jump_to GOTO_G end
clone push rbx jump_to GOTO_L

_start:
    mov rax 0
    push rax
    mov rax 17488
    push rax
    mov rax 16758
    push rax
    mov rax 16599
    push rax
    mov rax 16285
    push rax
    mov rax 16094
    push rax
    mov rax 15505
    push rax
    mov rax 15417
    push rax
    mov rax 14832
    push rax
    mov rax 14450
    push rax
    mov rax 13893
    push rax
    mov rax 13926
    push rax
    mov rax 13437
    push rax
    mov rax 12833
    push rax
    mov rax 12741
    push rax
    mov rax 12533
    push rax
    mov rax 11504
    push rax
    mov rax 11342
    push rax
    mov rax 10503
    push rax
    mov rax 10550
    push rax
    mov rax 10319
    push rax
    mov rax 975
    push rax
    mov rax 1007
    push rax
    mov rax 892
    push rax
    mov rax 893
    push rax
    mov rax 660
    push rax
    mov rax 743
    push rax
    mov rax 267
    push rax
    mov rax 344
    push rax
    mov rax 264
    push rax
    mov rax 339
    push rax
    mov rax 208
    push rax
    mov rax 216
    push rax
    mov rax 242
    push rax
    mov rax 172
    push rax
    mov rax 74
    push rax
    mov rax 49
    push rax
    mov rax 119
    push rax
    mov rax 113
    push rax
    mov rax 119
    push rax
    mov rax 106
    push rax
    mov rbx 1

    jmp _GOTO_A

    mov rax 98426
    push rax
    mov rax 97850
    push rax
    mov rax 97604
    push rax
    mov rax 97280
    push rax
    mov rax 96815
    push rax
    mov rax 96443
    push rax
    mov rax 96354
    push rax
    mov rax 95934
    push rax
    mov rax 94865
    push rax
    mov rax 94952
    push rax
    mov rax 94669
    push rax
    mov rax 94440
    push rax
    mov rax 93969
    push rax
    mov rax 93766
    push rax
    mov rbx 99
    
    jmp _GOTO_B

    mov rax 101141058
    push rax
    mov rax 101060206
    push rax
    mov rax 101030055
    push rax
    mov rax 100998966
    push rax
    mov rax 100887990
    push rax
    mov rax 100767085
    push rax
    mov rax 100707036
    push rax
    mov rax 100656111
    push rax
    mov rax 100404094
    push rax
    mov rax 100160922
    push rax
    mov rax 100131019
    push rax
    mov rax 100111100
    push rax
    mov rax 100059926
    push rax
    mov rax 100049982
    push rax
    mov rax 100030045
    push rax
    mov rax 9989997
    push rax
    mov rax 9981858
    push rax
    mov rax 9980815
    push rax
    mov rax 9978842
    push rax
    mov rax 9965794
    push rax
    mov rax 9957564
    push rax
    mov rax 9938304
    push rax
    mov rax 9935427
    push rax
    mov rax 9932289
    push rax
    mov rax 9931494
    push rax
    mov rax 9927388
    push rax
    mov rax 9926376
    push rax
    mov rax 9923213
    push rax
    mov rax 9921394
    push rax
    mov rax 9919154
    push rax
    mov rax 9918082
    push rax
    mov rax 9916239
    push rax
    mov rbx 765

    jmp _GOTO_C
