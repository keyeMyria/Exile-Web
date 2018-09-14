import { Component, OnInit, OnChanges } from '@angular/core';
import { TareaService } from './tarea.service';

declare var _server: string
declare var $: any;

@Component({
    templateUrl: './tarea.component.html',
    styleUrls: ['./tarea.component.scss']
})
export class TareaComponent implements OnInit, OnChanges {

    public notificacion: any;
    public tarea: any;
    public step = 0;
    // public _selected = 0;
    //

    //
    // private color = '#555'
    // private selectNt: any;
    // private selectItem: any

    constructor(private _t: TareaService) { }

    // set selected(id: number) {
    //
    // }

    ngOnInit(): void {
        console.log('ok')
    }

    ngOnChanges(changes): void {
        console.log(changes)
    }

    onSelectItem(notificacion): void {
        this.notificacion = notificacion;
        this.tarea = this.notificacion.tarea;
        console.log(this.notificacion);

    }

    onLoad(last) {
        if (last) {
            setTimeout(() => {
                $('.bxslider').bxSlider({
                    slideWidth: 200,
                    minSlides: 2,
                    maxSlides: 3,
                    slideMargin: 10
                });
            }, 3000)
        }
    }

    onCheckSubTarea(event): void {
        console.log(event);
    }

    onCheckTarea(event): void {
        console.log(event);
        this.notificacion.completado = event.checked;
    }

    stop(e): void {
        event.stopPropagation();
    }

    setStep(index: number): void {
        this.step = index;
    }

    nextStep(): void {
        this.step++;
    }

    prevStep(): void {
        this.step--;
    }

    get multimediaImages() {
        let images = [];
        if (!!this.notificacion) {
            images = this.notificacion.multimedia.filter(item => item.tipo === TareaService.FOTO);
        }
        return images;
    }

    get multimediaAudios() {
        let audios = [];
        if (!!this.notificacion) {
            audios = this.notificacion.multimedia.filter(item => item.tipo === TareaService.AUDIO);
        }
        return audios;
    }
}
