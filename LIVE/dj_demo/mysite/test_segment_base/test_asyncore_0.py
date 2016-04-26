# used when testing senders; just collects what it gets until newline is sent
def capture_server(evt, buf, serv):
    try:
        serv.listen(5)
        conn, addr = serv.accept()
    except socket.timeout:
        pass
    else:
        n = 200
        while n > 0:
            r, w, e = select.select([conn], [], [])
            if r:
                data = conn.recv(10)
                # keep everything except for the newline terminator
                buf.write(data.replace('\n', ''))
                if '\n' in data:
                    break
            n -= 1
            time.sleep(0.01)
        conn.close()
    finally:
        serv.close()
        evt.set()
