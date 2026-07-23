# System Architecture Notes

Notes on two things I wanted to understand properly: how the OSI model works and why it's not actually what runs the internet, and what really happens when you click something on a computer, all the way down to the kernel and back.

## The OSI Model

OSI stands for Open Systems Interconnection. It's a 7 layer model used to describe how data moves across a network. The layers are:

1. Application - closest to the user. Browsers, email apps, anything with an interface. HTTP, FTP and SMTP work at this level.
2. Presentation - deals with formatting, encryption and translating data so different systems can understand each other.
3. Session - keeps track of the connection between two devices, opening and closing it.
4. Transport - responsible for getting data from one end to the other, in order and reliably. TCP and UDP work here.
5. Network - handles addressing and routing between different networks. This is where IP lives.
6. Data Link - handles delivery between devices on the same network, and MAC addressing.
7. Physical - the actual hardware, cables, signals, the bits travelling on the wire.

### Why it's not used in production

OSI was built as a reference model, meant to describe networking in theory. The problem is it was designed before most of the protocols we actually use existed, so it doesn't match reality that well:

- The Session and Presentation layers barely exist in practice. Most protocols handle sessions and formatting themselves instead of following OSI's separation. HTTP manages its own sessions with cookies, TLS handles encryption wherever it fits in the stack.
- By the time OSI was finished, TCP/IP was already running real networks. So OSI ended up as a theory built around a system that already existed a different way.
- Splitting everything into 7 layers adds overhead that real systems don't want. It's cleaner in a textbook than it is in a router.

Because of this, OSI is mostly used today as a teaching model, a way to talk about which layer a problem is happening at. It's not literally what's implemented in real hardware or software.

### What's actually used: TCP/IP

The model that's actually running the internet is TCP/IP, and it only has 4 layers:

1. Application - combines OSI's Application, Presentation and Session layers into one. HTTP, DNS, SSH all sit here.
2. Transport - same job as in OSI. TCP for reliable delivery, UDP for speed with no guarantees.
3. Internet - same as OSI's Network layer. Handles IP addressing and routing.
4. Link - combines OSI's Data Link and Physical layers. This is where the operating system passes data to the actual network hardware.

TCP/IP won out because it was built alongside the protocols it describes, not designed on paper first. Real operating systems, including Linux, structure their networking around these 4 layers.

## From clicking something to the kernel and back

This is the part that actually made networking and OS concepts click for me, tracing what happens after something as small as a mouse click.

**Step 1 - The click itself**
Clicking a mouse button sends an electrical signal from the hardware, which gets turned into an interrupt. The CPU stops what it's doing and the kernel's interrupt handler picks up the raw input.

**Step 2 - Kernel passes it up**
The kernel sends this raw event through its input subsystem (evdev on Linux, for example) to the display server or compositor, whatever is managing windows on screen. This part figures out which window was actually clicked based on what's visible and where.

**Step 3 - It reaches the app**
The display server routes the event to the application that owns the window. Inside the app, whatever GUI toolkit it's built with turns that event into the actual function you wrote for the click, like an onClick handler.

**Step 4 - The app runs its own code**
This runs in userspace, meaning the app is only using the memory and CPU time that belongs to it. If the click needs to read a file or reach the network, the app can't do that directly, those are privileged actions only the kernel is allowed to perform.

**Step 5 - Crossing into the kernel**
So the app makes a system call, something like read, write or socket. This causes a mode switch, the CPU flips from user mode to kernel mode so the kernel can safely handle the request with higher privileges.

**Step 6 - Memory gets involved**
If memory is needed, the kernel finds free physical memory and updates the process's page tables. The process itself only ever sees virtual addresses, the CPU's memory management unit (MMU) translates these into real physical addresses behind the scenes. This is also why one process can't read another process's memory, each one only maps to its own physical memory. Addressing modes come in at the instruction level, they're just the different ways an instruction can calculate the address it wants to access (direct, indirect, using an offset, etc), before the MMU translates it.

**Step 7 - The kernel does the actual work**
Depending on what was requested, the kernel talks to the filesystem and disk driver, or the network stack. If it's a network request, this is where the TCP/IP layers from earlier come in, the data gets wrapped into a TCP segment, then an IP packet, then a frame, before actually leaving through the network hardware.

**Step 8 - Coming back up**
Once the kernel is done, it copies the result back into the app's memory, switches the CPU back to user mode, and the app continues running from where it left off. The app then updates whatever needs to change on screen, and the GUI toolkit and display server redraw it. That final image gets pushed to the framebuffer, and the graphics driver hands it to the GPU, which puts it on the actual screen.

So overall it goes: click, interrupt, kernel, display server, app, system call, kernel handles memory/disk/network, back to the app, back to the screen. Every step exists because of some boundary being protected, hardware and kernel, kernel and app, one process and another. Once I understood why those boundaries exist, the whole flow made a lot more sense than just memorising the steps.
