import { Component, EventEmitter, Input, NgZone, OnInit, Output, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { BehaviorSubject, take } from 'rxjs';

import { RawReview } from '../review';
import { CdkTextareaAutosize } from '@angular/cdk/text-field';

@Component({
  selector: 'app-review-form',
  templateUrl: './review-form.component.html',
  styleUrls: ['./review-form.component.scss']
})
export class ReviewFormComponent implements OnInit {
  @Input()
  initialState: BehaviorSubject<Partial<RawReview>> = new BehaviorSubject({});

  @Output()
  formValuesChanged = new EventEmitter<RawReview>();

  @Output()
  formSubmitted = new EventEmitter<RawReview>();

  reviewForm: FormGroup;

  @ViewChild('autosize') autosize: CdkTextareaAutosize;

  get name() { return this.reviewForm.get('name')!; }
  get text() { return this.reviewForm.get('text')!; }

  constructor(
    private fb: FormBuilder,
  ) { }

  ngOnInit(): void {
    this.initialState.subscribe(review => {
      this.reviewForm = this.fb.group({
        name: [ review.name, [Validators.required] ],
        text: [ review.text, [ Validators.required, Validators.minLength(10) ] ],
      });
    });
  }

  submitForm() {
    this.formSubmitted.emit({
      ...this.reviewForm.value,
      date: new Date()
    });

    this.reviewForm.reset();
  }
}