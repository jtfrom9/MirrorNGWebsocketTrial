using System;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Mirror.Websocket;
using Cysharp.Threading.Tasks;

public class WebsocketServer : MonoBehaviour
{
    [SerializeField] WsTransport transport;
    async void Start()
    {
        int id = 1;
        transport.Connected.AddListener(async (c) =>
        {
            Debug.Log($"connected. {c.GetEndPointAddress()}");
            // var ms = new MemoryStream(Encoding.UTF8.GetBytes("hello from unity"));
            var seg = new ArraySegment<byte>(Encoding.UTF8.GetBytes($"hello from Unity ({id})"));
            await c.SendAsync(seg);

            var ms = new MemoryStream();
            await c.ReceiveAsync(ms);
            Debug.Log($"recve from client: {Encoding.UTF8.GetString(ms.ToArray())}");
            id++;
        });

        Debug.Log("wait for listen...");
        await transport.ListenAsync();
        Debug.Log("connected.");
    }
}
