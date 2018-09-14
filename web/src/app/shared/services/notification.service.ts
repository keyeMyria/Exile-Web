import { Injectable } from '@angular/core';
import { WebsocketService } from './call.service';
import { Subject } from 'rxjs/Rx';

@Injectable()
export class NotificationService {
    list: any[] = [];
    constructor(private _ws: WebsocketService){
        this._ws.mgs().subscribe(data => {
            this.list.push(data);
        });
    }
}